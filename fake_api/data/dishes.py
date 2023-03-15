import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Dishes(SqlAlchemyBase):
    __tablename__ = 'dishes'
    __table_args__ = {'extend_existing': True}

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("groups.id"))
    group = orm.relationship("Groups", foreign_keys="Dishes.group_id")

    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)

# TODO LOCATION_ID, IMAGE_URL
