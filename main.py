import os
from dotenv import load_dotenv
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, User, InputMediaPhoto
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    PreCheckoutQueryHandler
)

from handlers.menu_maker import process_menu_selection, create_group_menu
from handlers.dish_page import process_dish_selection
from handlers.order import process_order_selection

load_dotenv()
TOKEN = os.environ["TELEGRAM_TOKEN"]


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Далее", callback_data="home")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        '''Привет!
Здесь ты можешь заказать еду в столовой.
Выбирай категорию блюд, нажимай на интересующее, регулируй количество и нажимай "Добавить в корзину".
Как соберешь все нужные для тебя блюда - переходи в корзину и оплачивай заказ.
№ заказа высветится на табло!
Приятного аппетита!
Если ознокомились, нажмите кнопку "Далее"''',
        reply_markup=reply_markup)


async def button(update, context):
    query = update.callback_query
    await query.answer()
    if query.data == "home":
        await home(update, context)

    elif query.data[:5] == "ORDER":
        await process_order_selection(update, context)

    elif query.data[:4] == "MENU":
        await process_menu_selection(update, context)

    elif query.data[:8] == "DISHPAGE":
        await process_dish_selection(update, context)


async def home(update, context):
    reply_markup = create_group_menu(update.callback_query.from_user.id)
    await update.callback_query.edit_message_text("Выберите блюдо\nМинимальная сумма заказа 100₽",
                                                  reply_markup=reply_markup)


async def pre_checkout_query(update, context):
    await context.bot.answer_pre_checkout_query(update.pre_checkout_query.id, ok=True)


async def process_successful_payment(update, context):
    payload = update.message.successful_payment.invoice_payload

    await context.bot.send_message(text="Заказ успешно оплачен\n"
                                        f"Номер заказа: {payload}\n"
                                        f"Для повторного заказа нажмите /start", chat_id=update.message.chat_id)



def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(PreCheckoutQueryHandler(pre_checkout_query))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, process_successful_payment))
    application.run_polling()


if __name__ == "__main__":
    main()
