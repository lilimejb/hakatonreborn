from flask import Flask, render_template, redirect, request, abort
from data import db_session, fake_ikko_api
from flask_restful import Api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'stolovka'

db_session.global_init("db/dishes.db")


def main():
    api.add_resource(fake_ikko_api.DishResource, '/api/dish/<int:dish_id>')
    api.add_resource(fake_ikko_api.AllDishResource, '/api/dish/all/<int:group_id>')
    api.add_resource(fake_ikko_api.ComboResource, '/api/combo/<int:combo_id>')
    api.add_resource(fake_ikko_api.AllComboResource, '/api/combo/all')
    api.add_resource(fake_ikko_api.GroupResource, '/api/group/<int:group_id>')
    api.add_resource(fake_ikko_api.AllGroupResource, '/api/group/all')
    app.run(debug=True)


if __name__ == '__main__':
    main()
