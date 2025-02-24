from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import AuditLog, License, User


def test_create_log(session: Session) -> None:
    audit_log = AuditLog(
        performed_by_id=1,
        entity_id=1,
        entity='License',
        action='delete',
    )

    session.add(audit_log)
    session.commit()

    assert audit_log is not None
    assert audit_log.timestamp is not None


def test_read_log(
    audit_log: AuditLog, user: User, mock_license: License
) -> None:
    assert audit_log.performed_by_id == user.id
    assert audit_log.entity_id == mock_license.id
    assert audit_log.entity == 'License'
    assert audit_log.action == 'delete'


def test_delete_log(session: Session, audit_log: AuditLog) -> None:
    session.delete(audit_log)
    session.commit()

    result = session.scalar(
        select(AuditLog).where(AuditLog.id == audit_log.id)
    )

    assert result is None


def test_update_log(session: Session, audit_log: AuditLog) -> None:
    audit_log.action = 'update'
    session.commit()
    session.refresh(audit_log)

    assert audit_log.action == 'update'
