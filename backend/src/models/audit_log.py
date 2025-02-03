from datetime import datetime

from sqlalchemy import TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry


@table_registry.mapped_as_dataclass
class AuditLog:
    __tablename__ = 'audit_logs'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    performed_by_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    entity_id: Mapped[int]
    entity: Mapped[str]
    action: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        nullable=True,
        onupdate=func.now(),
    )

    # relacionamentos
    performed_by = relationship('User', back_populates='audit_logs')
