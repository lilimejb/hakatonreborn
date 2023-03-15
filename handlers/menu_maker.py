from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from hakatonreborn.working_with_api.api import Api
from hakatonreborn.handlers.dish_page import create_dish_page
from hakatonreborn.handlers.utils import *

api = Api()


def create_group_menu(current_user):
    keyboard = [[InlineKeyboardButton("Ваша корзина",
                                      callback_data=create_order_callback_data("IGNORE", current_user))]]
    all_groups = api.get_all_groups()["groups"]
    for i in range(0, len(all_groups), 2):
        try:
            keyboard.append([
                InlineKeyboardButton(f"{all_groups[i]['name']}",
                                     callback_data=create_menu_callback_data("DISH", all_groups[i]['id'], None)),
                InlineKeyboardButton(f"{all_groups[i + 1]['name']}",
                                     callback_data=create_menu_callback_data("DISH", all_groups[i + 1]['id'], None))])
        except IndexError:
            keyboard.append([
                InlineKeyboardButton(f"{all_groups[i]['name']}",
                                     callback_data=create_menu_callback_data("DISH", all_groups[i]['id'], None))])
    return InlineKeyboardMarkup(keyboard)


def create_dish_menu(group_id):
    dishboard = []
    dishes = api.get_all_dishes(group_id)["dishes"]
    for i in range(len(dishes)):
        dishboard.append([
                InlineKeyboardButton(f"{dishes[i]['name']} - {dishes[i]['price']}",
                                     callback_data=create_menu_callback_data("OK", dishes[i]['group_id'], dishes[i]['id']))])
    keyboard = [
        *dishboard,
        [
            InlineKeyboardButton("Назад", callback_data=create_menu_callback_data(
                "BACK", group_id, None))
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


async def process_menu_selection(update, context):
    query = update.callback_query
    await query.answer()
    (_, action, group_id, dish_id) = separate_callback_data(query.data)
    if action == "OK":
        keyboard, text = create_dish_page(dish_id, group_id, 1)
        await context.bot.edit_message_text(text=text,
                                            chat_id=query.message.chat_id,
                                            message_id=query.message.message_id,
                                            reply_markup=keyboard)
    elif action == "DISH":
        await context.bot.edit_message_text(text=query.message.text,
                                            chat_id=query.message.chat_id,
                                            message_id=query.message.message_id,
                                            reply_markup=create_dish_menu(group_id))
    elif action == "BACK":
        await context.bot.edit_message_text(text="Выберите блюдо\nМинимальная сумма заказа 100₽",
                                            chat_id=query.message.chat_id,
                                            message_id=query.message.message_id,
                                            reply_markup=create_group_menu(query.from_user.id))
    else:
        await context.bot.answer_callback_query(callback_query_id=query.id, text="Что-то пошло не так")
