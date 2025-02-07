from datetime import datetime

from sqlalchemy import ForeignKey, Text, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry


@table_registry.mapped_as_dataclass
class Notification:
    __tablename__ = 'notifications'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey(
            'users.id', name='fk_notifications_user_id', ondelete='CASCADE'
        )
    )
    license_id: Mapped[int] = mapped_column(
        ForeignKey(
            'licenses.id',
            name='fk_notifications_license_id',
            ondelete='CASCADE',
        ),
        nullable=True,
    )
    request_id: Mapped[int] = mapped_column(
        ForeignKey(
            'renewal_requests.id',
            name='fk_notifications_request_id',
            ondelete='CASCADE',
        ),
        nullable=True,
    )
    message: Mapped[str] = mapped_column(Text)
    is_read: Mapped[bool] = mapped_column(
        init=False, server_default=text('false')
    )
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )

    # relacionametos
    recipient_user = relationship('User', back_populates='notifications')
    about_license = relationship('License', back_populates='notifications')
    about_request = relationship(
        'RenewalRequest', back_populates='notifications'
    )
