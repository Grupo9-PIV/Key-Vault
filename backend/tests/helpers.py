from datetime import datetime

from sqlalchemy.orm import Session

from src.models import License, User


def add_user(session: Session) -> None:
    user = User(
        email='teste@teste.com',
        password_hash='12345678',
        name='Teste',
        role='admin',
        department='Teste',
    )
    session.add(user)
    session.commit()


def add_license(session: Session) -> None:
    mock_license = License(
        assigned_to_id=1,
        manager_id=1,
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
