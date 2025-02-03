from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import License
from tests.helpers import add_license


def test_create_license(session_with_user: Session) -> None:
    add_license(session_with_user)

    result = session_with_user.scalar(select(License).where(License.id == 1))

    assert result.id == 1
    assert result.software_name == 'XYZ Soft'
    assert result.purchase_date.strftime('%d/%m/%Y') == '01/01/1900'
    assert result.updated_at is None


def test_delete_license(session_with_user_and_license: Session) -> None:
    mock_license = session_with_user_and_license.scalar(
        select(License).where(License.id == 1)
    )
    assert mock_license is not None

    session_with_user_and_license.delete(mock_license)
    session_with_user_and_license.commit()

    result = session_with_user_and_license.scalar(
        select(License).where(License.id == 1)
    )
    assert result is None


def test_update_license(session_with_user_and_license) -> None:
    mock_license = session_with_user_and_license.scalar(
        select(License).where(License.id == 1)
    )
    assert mock_license is not None

    mock_license.software_name = 'New Soft'
    mock_license.version = 'v1.0.1'

    session_with_user_and_license.commit()
    session_with_user_and_license.refresh(mock_license)

    updated_license = session_with_user_and_license.scalar(
        select(License).where(License.id == 1)
    )

    assert updated_license.software_name == 'New Soft'
    assert updated_license.version == 'v1.0.1'
    assert updated_license.updated_at is not None
