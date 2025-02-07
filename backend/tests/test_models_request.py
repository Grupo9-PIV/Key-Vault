from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import License, Notification, RenewalRequest, User
from src.models.renewal_request import DEFAULT_STATUS


def test_create_request(
    session: Session, mock_license: License, user: User
) -> None:
    request = RenewalRequest(
        license_id=mock_license.id,
        requested_by_id=user.id,
        manager_id=user.id,
        reason=None,
        feedback=None,
        status=DEFAULT_STATUS,
    )

    session.add(request)
    session.commit()

    result = session.scalar(
        select(RenewalRequest).where(RenewalRequest.id == request.id)
    )

    assert result is not None
    assert result.request_license == mock_license
    assert result.managed_by == user
    assert result.requested_by == user
    assert result.created_at is not None
    assert result.updated_at is None


def test_delete_request(
    session: Session, renewal_request: RenewalRequest
) -> None:
    session.delete(renewal_request)
    session.commit()

    deleted_request = session.scalar(
        select(RenewalRequest).where(RenewalRequest.id == renewal_request.id)
    )

    assert deleted_request is None


def test_update_request(
    session: Session, renewal_request: RenewalRequest
) -> None:
    renewal_request.reason = 'Important license'
    renewal_request.feedback = 'Nope'
    renewal_request.status = 'rejeitada'

    session.commit()
    session.refresh(renewal_request)

    assert renewal_request.reason == 'Important license'
    assert renewal_request.feedback == 'Nope'
    assert renewal_request.status == 'rejeitada'
    assert renewal_request.updated_at is not None


def test_renewal_request_relationships(
    session: Session,
    user: User,
    mock_license: License,
    notification: Notification,
    renewal_request: RenewalRequest,
) -> None:
    notification.about_request = renewal_request

    session.commit()
    session.refresh(notification)

    assert notification in renewal_request.notifications
    assert renewal_request in user.requests
    assert renewal_request in mock_license.requests


def test_default_status_pendente(session: Session) -> None:
    renewal_request = RenewalRequest(
        license_id=None,
        requested_by_id=None,
        manager_id=None,
        reason=None,
        feedback=None,
        status=None,
    )
    session.add(renewal_request)
    session.commit()
    session.refresh(renewal_request)

    assert renewal_request.status == DEFAULT_STATUS


def test_user_and_license_delete_set_null(
    session: Session,
    user: User,
    mock_license: License,
    renewal_request: RenewalRequest,
) -> None:
    session.delete(user)
    session.delete(mock_license)
    session.commit()
    session.refresh(renewal_request)

    assert renewal_request.license_id is None
    assert renewal_request.requested_by_id is None
