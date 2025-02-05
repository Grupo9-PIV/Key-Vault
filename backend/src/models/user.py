from datetime import datetime

from sqlalchemy import func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str]
    name: Mapped[str]
    role: Mapped[str]
    department: Mapped[str] = mapped_column(nullable=True)
    is_first_login: Mapped[bool] = mapped_column(
        init=False, server_default=text('true')
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        init=False,
        nullable=True,
        onupdate=func.now(),
    )

    # relacionamentos
    licenses = relationship(
        'License',
        back_populates='assigned_to',
        primaryjoin='User.id == License.assigned_to_id',
        cascade='save-update',
        passive_deletes=True,
    )
    managed_licenses = relationship(
        'License',
        back_populates='managed_by',
        primaryjoin='User.id == License.manager_id',
        cascade='save-update',
        passive_deletes=True,
    )
    requests = relationship(
        'RenewalRequest',
        back_populates='requested_by',
        primaryjoin='User.id == RenewalRequest.requested_by_id',
        cascade='save-update',
        passive_deletes=True,
    )
    managed_requests = relationship(
        'RenewalRequest',
        back_populates='managed_by',
        primaryjoin='User.id == RenewalRequest.manager_id',
        cascade='save-update',
        passive_deletes=True,
    )
    notifications = relationship(
        'Notification',
        back_populates='recipient_user',
        cascade='all, delete-orphan',
    )
