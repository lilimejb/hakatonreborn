import flask
from flask import jsonify

from . import db_session
from .dishes import Dishes
from .groups import Groups
from .combos import Combos
from flask_restful import abort, Resource

blueprint = flask.Blueprint(
    'fake_ikko_api',
    __name__,
    template_folder='templates'
)


def abort_if_not_found(id, object_name):
    session = db_session.create_session()
    request = session.query(object_name).get(id)
    if not request:
        abort(400, message=f"{object_name.__tablename__} {id} not found")


class DishResource(Resource):
    def get(self, dish_id):
        abort_if_not_found(dish_id, Dishes)
        session = db_session.create_session()
        dish = session.query(Dishes).get(dish_id)
        name, group_id, price, description = dish.name, dish.group_id, dish.price, dish.description
        return jsonify({"dish":
                        {"name": name,
                         "group_id": group_id,
                         "price": price,
                         "description": description}})


class AllDishResource(Resource):
    def get(self, group_id):
        session = db_session.create_session()
        dishes = session.query(Dishes).filter(Dishes.group_id == group_id).all()
        dish_list = []
        for dish in dishes:
            dish_id, name, group_id, price, description \
                = dish.id, dish.name, dish.group_id, dish.price, dish.description
            dish_list.append(
                {"id": dish_id,
                 "name": name,
                 "group_id": group_id,
                 "price": price,
                 "description": description})

        return jsonify({"dishes": dish_list})


class GroupResource(Resource):
    def get(self, group_id):
        abort_if_not_found(group_id, Groups)
        session = db_session.create_session()
        group = session.query(Groups).get(group_id)
        return jsonify({"groups": {"id": group.id, "name": group.name}})


class AllGroupResource(Resource):
    def get(self):
        session = db_session.create_session()
        groups = session.query(Groups).all()
        group_list = []
        for group in groups:
            group_list.append(
                {"id": group.id,
                 "name": group.name})

        return jsonify({"groups": group_list})


class ComboResource(Resource):
    def get(self, combo_id):
        session = db_session.create_session()
        combo = session.query(Combos).get(combo_id)
        return jsonify({"combos": {"id": combo.id,
                                   "soup_id": combo.soup_id,
                                   "main_dish_id": combo.main_dish_id,
                                   "side_dish_id": combo.side_dish_id,
                                   "salad_id": combo.salad_id,
                                   "drink_id": combo.drink_id,
                                   "price": combo.price,
                                   "description": combo.description}})


class AllComboResource(Resource):
    def get(self):
        session = db_session.create_session()
        combos = session.query(Combos).all()
        combo_list = []
        for combo in combos:
            combo_id, soup_id, main_dish_id, side_dish_id, salad_id, drink_id, price, description = combo.id, \
                combo.soup_id, combo.main_dish_id, combo.side_dish_id, combo.salad_id, combo.drink_id, combo.price, \
                combo.description
            combo_list.append(
                {"id": combo_id,
                 "soup_id": soup_id,
                 "main_dish_id": main_dish_id,
                 "side_dish_id": side_dish_id,
                 "salad_id": salad_id,
                 "drink_id": drink_id,
                 "price": price,
                 "description": description})

        return jsonify({"dishes": combo_list})
