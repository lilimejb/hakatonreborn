DISH_CALLBACK = "DISHPAGE"
MENU_CALLBACK = "MENU"
ORDER_CALLBACK = "ORDER"
carts = []


def create_dish_callback_data(action, dish_id, group_id, amount):
    return DISH_CALLBACK + ";" + ";".join([action,  str(group_id), str(dish_id), str(amount)])


def create_menu_callback_data(action, group_id, dish_id):
    return MENU_CALLBACK + ";" + ";".join([action, str(group_id), str(dish_id)])


def create_order_callback_data(action, user_id):
    return ORDER_CALLBACK + ";" + ";".join([action, str(user_id)])


def separate_callback_data(callback_data):
    return callback_data.split(";")


def create_cart_data(name, price, amount):
    return {"name": name, "price": price, "amount": amount}

