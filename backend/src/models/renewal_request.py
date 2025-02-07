from datetime import datetime

from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry

DEFAULT_STATUS = 'pendente'


@table_registry.mapped_as_dataclass
class RenewalRequest:
    __tablename__ = 'renewal_requests'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    license_id: Mapped[int] = mapped_column(
        ForeignKey(
            'licenses.id',
            name='fk_renewal_requests_license_id',
            ondelete='SET NULL',
        ),
        nullable=True,
    )
    requested_by_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.id',
            name='fk_renewal_requests_requested_by_id',
            ondelete='SET NULL',
        ),
        nullable=True,
    )
    manager_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.id',
            name='fk_renewal_requests_manager_id',
            ondelete='SET NULL',
        ),
        nullable=True,
    )
    reason: Mapped[str] = mapped_column(Text, nullable=True)
    feedback: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(default=DEFAULT_STATUS)
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        nullable=True,
        onupdate=func.now(),
    )

    # relacionametos
    request_license = relationship('License', back_populates='requests')
    requested_by = relationship(
        'User', back_populates='requests', foreign_keys=[requested_by_id]
    )
    managed_by = relationship(
        'User', back_populates='managed_requests', foreign_keys=[manager_id]
    )
    notifications = relationship(
        'Notification',
        back_populates='about_request',
        cascade='all, delete-orphan',
    )
