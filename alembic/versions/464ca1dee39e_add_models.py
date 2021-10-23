"""add models

Revision ID: 464ca1dee39e
Revises: 
Create Date: 2021-10-23 17:19:32.200510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '464ca1dee39e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fk_note_user_idx', table_name='note')
    op.drop_index('id_UNIQUE', table_name='note')
    op.drop_constraint('fk_note_connected_user1', 'note', type_='foreignkey')
    op.drop_constraint('fk_note_user', 'note', type_='foreignkey')
    op.drop_index('fk_note_history_Action1_idx', table_name='note_log')
    op.drop_index('fk_note_history_note1_idx', table_name='note_log')
    op.drop_index('id_UNIQUE', table_name='note_log')
    op.drop_constraint('fk_note_history_note1', 'note_log', type_='foreignkey')
    op.drop_constraint('fk_note_history_Action1', 'note_log', type_='foreignkey')
    op.drop_index('id_UNIQUE', table_name='user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('id_UNIQUE', 'user', ['id'], unique=False)
    op.create_foreign_key('fk_note_history_Action1', 'note_log', 'action', ['action_id'], ['id'])
    op.create_foreign_key('fk_note_history_note1', 'note_log', 'note', ['note_id'], ['id'])
    op.create_index('id_UNIQUE', 'note_log', ['id'], unique=False)
    op.create_index('fk_note_history_note1_idx', 'note_log', ['note_id'], unique=False)
    op.create_index('fk_note_history_Action1_idx', 'note_log', ['action_id'], unique=False)
    op.create_foreign_key('fk_note_user', 'note', 'user', ['user_id'], ['id'])
    op.create_foreign_key('fk_note_connected_user1', 'note', 'connected_user', ['id'], ['note_id'])
    op.create_index('id_UNIQUE', 'note', ['id'], unique=False)
    op.create_index('fk_note_user_idx', 'note', ['user_id'], unique=False)
    # ### end Alembic commands ###
