from datetime import datetime

from sqlalchemy import Enum, ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry
from src.enums import LicensePriority, LicenseStatus, LicenseType

DEFAULT_PRIORITY = LicensePriority.MEDIA


@table_registry.mapped_as_dataclass
class License:
    __tablename__ = 'licenses'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    assigned_to_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.id', name='fk_licenses_assigned_to_id', ondelete='SET NULL'
        ),
        nullable=True,
    )
    manager_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.id', name='fk_licenses_manager_id', ondelete='SET NULL'
        ),
        nullable=True,
    )
    software_name: Mapped[str]
    license_type: Mapped[LicenseType] = mapped_column(Enum(LicenseType))
    status: Mapped[LicenseStatus] = mapped_column(Enum(LicenseStatus))
    developed_by: Mapped[str]
    version: Mapped[str] = mapped_column(nullable=True)
    purchase_date: Mapped[datetime] = mapped_column(server_default=func.now())
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
    priority: Mapped[LicensePriority] = mapped_column(
        Enum(LicenseType), default=DEFAULT_PRIORITY
    )

    # relacionamentos
    assigned_to = relationship(
        'User', back_populates='licenses', foreign_keys=[assigned_to_id]
    )
    managed_by = relationship(
        'User', back_populates='managed_licenses', foreign_keys=[manager_id]
    )
    requests = relationship(
        'RenewalRequest',
        back_populates='request_license',
        cascade='save-update',
        passive_deletes=True,
    )
    notifications = relationship(
        'Notification',
        back_populates='about_license',
        cascade='all, delete-orphan',
    )
