import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models import License, Notification, RenewalRequest, User


def test_create_notification(session: Session, user: User) -> None:
    notification = Notification(
        user_id=user.id,
        license_id=None,
        request_id=None,
        message='Test Notification',
    )
    session.add(notification)
    session.commit()

    result = session.scalar(
        select(Notification).where(Notification.id == notification.id)
    )
    assert result is not None
    assert result.message == 'Test Notification'
    assert result.user_id == user.id
    assert not result.is_read
    assert result.created_at is not None


def test_delete_notification(
    session: Session, notification: Notification
) -> None:
    session.delete(notification)
    session.commit()

    deleted_notification = session.scalar(
        select(Notification).where(Notification.id == notification.id)
    )
    assert deleted_notification is None


def test_update_notification(
    session: Session, notification: Notification
) -> None:
    notification.message = 'Updated Message'
    notification.is_read = True
    session.commit()
    session.refresh(notification)

    updated_notification = session.scalar(
        select(Notification).where(Notification.id == notification.id)
    )
    assert updated_notification.message == 'Updated Message'
    assert updated_notification.is_read is True


def test_notification_relationships(
    session: Session,
    user: User,
    mock_license: License,
    renewal_request: RenewalRequest,
) -> None:
    notification = Notification(
        user_id=user.id,
        license_id=mock_license.id,
        request_id=renewal_request.id,
        message='Test Notification',
    )
    session.add(notification)
    session.commit()

    assert notification.recipient_user == user
    assert notification.about_license == mock_license
    assert notification.about_request == renewal_request
    assert notification in user.notifications
    assert notification in mock_license.notifications
    assert notification in renewal_request.notifications


def test_missing_required_fields(session: Session) -> None:
    notification = Notification(
        user_id=None,
        license_id=None,
        request_id=None,
        message=None,
    )
    session.add(notification)

    with pytest.raises(IntegrityError):
        session.commit()


def test_created_at_not_updated(
    session: Session, notification: Notification
) -> None:
    original_created_at = notification.created_at
    notification.message = 'Updated Message'
    session.commit()
    session.refresh(notification)

    assert notification.created_at == original_created_at


def test_user_cascade_delete(
    session: Session, user: User, notification: Notification
) -> None:
    old_notification = notification
    session.delete(user)
    session.commit()

    deleted_notification = session.scalar(
        select(Notification).where(Notification.id == old_notification.id)
    )

    assert deleted_notification is None


def test_default_values(session: Session, user: User) -> None:
    notification = Notification(
        user_id=user.id,
        license_id=None,
        request_id=None,
        message='Test Notification',
    )
    session.add(notification)
    session.commit()

    assert not notification.is_read
    assert notification.created_at is not None
