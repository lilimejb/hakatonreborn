import os
from dotenv import load_dotenv
from telegram import LabeledPrice
from random import randint

load_dotenv()
PAYMENT_TOKEN = os.environ["PAYMENT_TOKEN"]


async def process_payment(update, context, price):
    if PAYMENT_TOKEN.split(":")[1] == "TEST":
        number = randint(1, 100)
        await context.bot.send_invoice(
            update.effective_chat.id,
            title="Оплата заказа",
            description=f"Заказ №{number}\n"
                        f"Для оплаты используйте данные тестовой карты:\n1111 1111 1111 1026,\n12/22,\nCVC -000.",
            currency="rub",
            provider_token=PAYMENT_TOKEN,
            prices=[LabeledPrice(label="Оплата заказа", amount=int(price) * 100)],
            payload=f"{number}"
        )


