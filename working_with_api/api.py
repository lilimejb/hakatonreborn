import requests
import json


class Api:

    def get_all_dishes(self, group_id):
        response = requests.get(f"http://127.0.0.1:5000/api/dish/all/{group_id}")
        return json.loads(response.text)

    def get_dish(self, dish_id):
        response = requests.get(f"http://127.0.0.1:5000/api/dish/{dish_id}")
        return json.loads(response.text)

    def get_all_combos(self):
        response = requests.get("http://127.0.0.1:5000/api/combo/all")
        return json.loads(response.text)

    def get_combo(self, combo_id):
        response = requests.get(f"http://127.0.0.1:5000/api/combo/{combo_id}")
        return json.loads(response.text)

    def get_all_groups(self):
        response = requests.get("http://127.0.0.1:5000/api/group/all")
        return json.loads(response.text)

    def get_group(self, group_id):
        response = requests.get(f"http://127.0.0.1:5000/api/group/{group_id}")
        return json.loads(response.text)


