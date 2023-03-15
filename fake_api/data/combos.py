import sqlalchemy

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Combos(SqlAlchemyBase):
    __tablename__ = 'combos'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    dish_id = "dishes.id"
    soup_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(dish_id))
    soup = orm.relationship("Dishes", foreign_keys="Combos.soup_id")
    main_dish_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(dish_id))
    main_dish = orm.relationship("Dishes", foreign_keys="Combos.main_dish_id")
    side_dish_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(dish_id))
    side_dish = orm.relationship("Dishes", foreign_keys="Combos.side_dish_id")
    salad_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(dish_id))
    salad = orm.relationship("Dishes", foreign_keys="Combos.salad_id")
    drink_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey(dish_id))
    drink = orm.relationship("Dishes", foreign_keys="Combos.drink_id")

    price = sqlalchemy.Column(sqlalchemy.Float, nullable=False)

    description = sqlalchemy.Column(sqlalchemy.String, nullable=False)

