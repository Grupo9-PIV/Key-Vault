from datetime import datetime

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.models import License, User


def test_create_license(session: Session, user: User) -> None:
    mock_license = License(
        assigned_to_id=user.id,
        manager_id=user.id,
        software_name='XYZ Soft',
        license_type='trial',
        status='ativa',
        developed_by='Test Soft',
        version='v1.0.0',
        purchase_date=datetime(1900, 1, 1),
        start_date=datetime(1900, 1, 1),
        end_date=datetime(1900, 1, 1),
        license_key=None,
        current_usage=None,
        subscription_plan=None,
        conditions=None,
    )
    session.add(mock_license)
    session.commit()

    result = session.scalar(select(License).where(License.id == 1))

    assert result.id == 1
    assert result.software_name == 'XYZ Soft'
    assert result.license_type == 'trial'
    assert result.status == 'ativa'
    assert result.developed_by == 'Test Soft'
    assert result.purchase_date.strftime('%d/%m/%Y') == '01/01/1900'
    assert result.updated_at is None


def test_delete_license(session: Session, mock_license: License) -> None:
    session.delete(mock_license)
    session.commit()

    deleted_license = session.scalar(
        select(License).where(License.id == mock_license.id)
    )
    assert deleted_license is None


def test_update_license(session: Session, mock_license: License) -> None:
    mock_license.software_name = 'New Soft'
    mock_license.version = 'v1.0.1'
    mock_license.license_type = 'perpetua'
    session.commit()
    session.refresh(mock_license)

    updated_license = session.scalar(
        select(License).where(License.id == mock_license.id)
    )
    assert updated_license.software_name == 'New Soft'
    assert updated_license.version == 'v1.0.1'
    assert updated_license.license_type == 'perpetua'
    assert updated_license.updated_at is not None


def test_license_user_relationship(user: User, mock_license: License) -> None:
    assert mock_license.assigned_to == user
    assert mock_license in user.licenses


def test_missing_required_fields(session: Session) -> None:
    mock_license = License(
        assigned_to_id=None,
        manager_id=None,
        software_name=None,
        license_type=None,
        status=None,
        developed_by=None,
        version=None,
        purchase_date=None,
        start_date=None,
        end_date=None,
        license_key=None,
        current_usage=None,
        subscription_plan=None,
        conditions=None,
    )
    session.add(mock_license)

    with pytest.raises(IntegrityError):
        session.commit()


def test_updated_at_auto_update(
    session: Session, mock_license: License
) -> None:
    original_updated_at = mock_license.updated_at
    mock_license.software_name = 'Updated Soft'
    session.commit()
    session.refresh(mock_license)

    assert mock_license.updated_at != original_updated_at
