"""'Init'

Revision ID: eee1c5024cdd
Revises: f2f905ab5e67
Create Date: 2023-10-07 01:01:14.450327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'eee1c5024cdd'
down_revision: Union[str, None] = 'f2f905ab5e67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('contacts', 'birthday',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.drop_index('ix_contacts_email', table_name='contacts')
    op.drop_index('ix_contacts_first_name', table_name='contacts')
    op.drop_index('ix_contacts_id', table_name='contacts')
    op.drop_index('ix_contacts_last_name', table_name='contacts')
    op.create_unique_constraint(None, 'contacts', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='unique')
    op.create_index('ix_contacts_last_name', 'contacts', ['last_name'], unique=False)
    op.create_index('ix_contacts_id', 'contacts', ['id'], unique=False)
    op.create_index('ix_contacts_first_name', 'contacts', ['first_name'], unique=False)
    op.create_index('ix_contacts_email', 'contacts', ['email'], unique=False)
    op.alter_column('contacts', 'birthday',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('contacts', 'phone',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('contacts', 'email',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    op.alter_column('contacts', 'last_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('contacts', 'first_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    # ### end Alembic commands ###
