from datetime import datetime

from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import table_registry


@table_registry.mapped_as_dataclass
class Notification:
    __tablename__ = 'notifications'

    # campos
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    license_id: Mapped[int] = mapped_column(
        ForeignKey('licenses.id'), nullable=True
    )
    request_id: Mapped[int] = mapped_column(
        ForeignKey('renewal_requests.id'), nullable=True
    )
    message: Mapped[str] = mapped_column(Text)
    is_read: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )

    # relacionametos
    recipient_user = relationship('User', back_populates='notifications')
    about_license = relationship('License', back_populates='notifications')
    about_request = relationship(
        'RenewalRequest', back_populates='notifications'
    )
