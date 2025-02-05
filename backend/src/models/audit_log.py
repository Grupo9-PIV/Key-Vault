from datetime import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import table_registry


@table_registry.mapped_as_dataclass
class AuditLog:
    __tablename__ = 'audit_logs'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    performed_by_id: Mapped[int]
    entity_id: Mapped[int]
    entity: Mapped[str]
    action: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        init=False,
        nullable=False,
        server_default=func.now(),
    )
