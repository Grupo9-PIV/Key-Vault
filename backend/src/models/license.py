from datetime import datetime

from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry

DEFAULT_PRIORITY = 'média'


@table_registry.mapped_as_dataclass
class License:
    __tablename__ = 'licenses'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    assigned_to_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=True)
    manager_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'), nullable=True)
    software_name: Mapped[str]
    license_type: Mapped[str]
    status: Mapped[str]
    developed_by: Mapped[str]
    version: Mapped[str] = mapped_column(nullable=True)
    purchase_date: Mapped[datetime]
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        nullable=True,
        onupdate=func.now(),
    )
    license_key: Mapped[str] = mapped_column(nullable=True)
    current_usage: Mapped[int] = mapped_column(nullable=True)
    subscription_plan: Mapped[str] = mapped_column(nullable=True)
    conditions: Mapped[str] = mapped_column(Text, nullable=True)
    priority: Mapped[str] = mapped_column(default=DEFAULT_PRIORITY)

    # relacionamentos
    assigned_to = relationship(
        'User', back_populates='licenses', foreign_keys=[assigned_to_id]
    )
    managed_by = relationship(
        'User', back_populates='managed_licenses', foreign_keys=[manager_id]
    )
