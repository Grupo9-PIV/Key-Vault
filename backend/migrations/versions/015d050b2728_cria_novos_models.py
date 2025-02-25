"""cria novos models

Revision ID: 015d050b2728
Revises: 17827d32fcaf
Create Date: 2025-02-03 11:43:31.277890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.enums import RequestStatus, AuditAction


# revision identifiers, used by Alembic.
revision: str = '015d050b2728'
down_revision: Union[str, None] = '17827d32fcaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audit_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('performed_by_id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('entity', sa.String(), nullable=False),
    sa.Column('action', sa.Enum(AuditAction), nullable=False),
    sa.Column('timestamp', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['performed_by_id'], ['users.id'], name='fk_audit_logs_performed_by_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('renewal_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('license_id', sa.Integer(), nullable=False),
    sa.Column('requested_by_id', sa.Integer(), nullable=False),
    sa.Column('manager_id', sa.Integer(), nullable=False),
    sa.Column('reason', sa.Text(), nullable=True),
    sa.Column('feedback', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum(RequestStatus), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['license_id'], ['licenses.id'], name='fk_renewal_requests_license_id'),
    sa.ForeignKeyConstraint(['manager_id'], ['users.id'], name='fk_renewal_requests_manager_id'),
    sa.ForeignKeyConstraint(['requested_by_id'], ['users.id'], name='fk_renewal_requests_requested_by_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('license_id', sa.Integer(), nullable=True),
    sa.Column('request_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.ForeignKeyConstraint(['license_id'], ['licenses.id'], name='fk_notifications_license_id'),
    sa.ForeignKeyConstraint(['request_id'], ['renewal_requests.id'], name='fk_notifications_request_id'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_notifications_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('department',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('department',
               existing_type=sa.VARCHAR(),
               nullable=False)

    op.drop_table('notifications')
    op.drop_table('renewal_requests')
    op.drop_table('audit_logs')
    # ### end Alembic commands ###
