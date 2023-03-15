from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from hakatonreborn.handlers.utils import *
from hakatonreborn.payments.pay import process_payment


def create_order(current_user):
    keyboard = [
        [
            InlineKeyboardButton("Оформить заказ", callback_data=create_order_callback_data("PAY", current_user))
        ],
        [
            InlineKeyboardButton("Очистить корзину", callback_data=create_order_callback_data("CLEAR", current_user))
        ],
        [
            InlineKeyboardButton("Назад", callback_data=create_menu_callback_data("BACK", None, None)),
        ]
    ]
    for cart in carts:
        if str(cart.get_userid()) == current_user:
            current_cart = dict(eval(repr(cart)))
            break
    else:
        current_cart = None

    if current_cart:
        text = "Ваш заказ:\n"
        for item in current_cart["items"]:
            text += f"\t{item['name']} - {float(item['price']) * int(item['amount'])}₽\n"
        text += f"В сумме {float(current_cart['total'])}₽\n"
    else:
        text = "Корзина пуста"

    return InlineKeyboardMarkup(keyboard), text


async def process_order_selection(update, context):
    callback_data = separate_callback_data(update.callback_query.data)
    (_, action, current_user) = callback_data

    if action == "PAY":
        for cart in carts:
            if str(cart.get_userid()) == current_user:
                current_cart = dict(eval(repr(cart)))
                break
        else:
            current_cart = None
        if current_cart:
            if int(current_cart["total"]) >= 100:
                await process_payment(update, context, current_cart["total"])
            else:
                keyboard, text = create_order(current_user)
                text += "\nМинимальная сумма заказа 100₽!!!"
                await update.callback_query.edit_message_text(
                    text=text,
                    reply_markup=keyboard)

    elif action == "CLEAR":
        for i in range(len(carts)):
            if str(carts[i].get_userid()) == current_user:
                carts.remove(carts[i])
                create_order(current_user)
                break
        keyboard, text = create_order(current_user)
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=keyboard)
    elif action == "IGNORE":
        keyboard, text = create_order(current_user)
        await update.callback_query.edit_message_text(
            text=text,
            reply_markup=keyboard)

