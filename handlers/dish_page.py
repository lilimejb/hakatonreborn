from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from hakatonreborn.working_with_api.api import Api
from hakatonreborn.handlers.utils import *
from hakatonreborn.handlers.cart import Cart

api = Api()


def create_dish_page(dish_id, group_id, amount):
    selectboard = [InlineKeyboardButton("-", callback_data=create_dish_callback_data("MINUS", dish_id, group_id, amount)),
                   InlineKeyboardButton("+", callback_data=create_dish_callback_data("PLUS", dish_id, group_id, amount))]
    dish = api.get_dish(dish_id)["dish"]
    keyboard = [selectboard,
                [
                    InlineKeyboardButton("В корзину", callback_data=create_dish_callback_data(
                        "TOCART", dish_id, group_id, amount))
                 ],
                [
                    InlineKeyboardButton("Назад", callback_data=create_menu_callback_data(
                        "BACK", group_id, dish_id))
                ]
                ]
    text = f"Блюдо: {dish['name']}\n" \
           f"Цена: {float(dish['price']) * int(amount)}₽\n" \
           f"Количество порций: {amount}\n" \
           f"{dish['description']}"

    return InlineKeyboardMarkup(keyboard), text


async def process_dish_selection(update, context):
    callback_data = separate_callback_data(update.callback_query.data)
    (_, action, group_id, dish_id, amount) = callback_data

    if action == "MINUS":
        amount = int(amount) - 1
    elif action == "PLUS":
        amount = int(amount) + 1
    elif action == "TOCART":
        current_user = update.callback_query.from_user.id
        dish = api.get_dish(dish_id)["dish"]
        for cart in carts:
            if cart.get_userid() == current_user:
                cart.add_item(create_cart_data(dish["name"], float(dish["price"]), int(amount)))
                break
        else:
            cart = Cart(current_user)
            cart.add_item(create_cart_data(dish["name"], dish["price"], amount))
            carts.append(cart)
        from hakatonreborn.handlers.menu_maker import create_group_menu
        keyboard = create_group_menu(current_user)
        await update.callback_query.edit_message_text(text="Выберите блюдо", reply_markup=keyboard)
        return

    else:
        await context.bot.answer_callback_query(callback_query_id=update.callback_query.id, text="Что-то пошло не так")

    keyboard, text = create_dish_page(dish_id, group_id, amount)
    await update.callback_query.edit_message_text(
        text=text,
        reply_markup=keyboard)
