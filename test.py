from pygrambot.updater import Updater
from pygrambot.handlers import MessageHandler
from pygrambot.types import Update
from config import TOKEN
import requests

def get_exchange_rates():
    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"  # CBU API
    response = requests.get(url)
    data = response.json()
    rates = {}
    for item in data:
        if item['Ccy'] == 'USD':
            rates['USD'] = float(item['Rate'].replace(',', ''))
        if item['Ccy'] == 'RUB':
            rates['RUB'] = float(item['Rate'].replace(',', ''))
    return rates

def handle_message(update: Update):
    if update.message.text:
        rates = get_exchange_rates()
        text = update.message.text.strip().lower()

        if 'usd' in text or '$' in text:
            amount = float(''.join(filter(str.isdigit, text)))
            result = amount * rates['USD']
            update.message.reply_text(f"{amount} USD ≈ {round(result)} so'm")

        elif 'so\'m' in text or 'uzs' in text:
            amount = float(''.join(filter(str.isdigit, text)))
            dollar = amount / rates['USD']
            update.message.reply_text(f"{amount} so'm ≈ {round(dollar, 2)} USD")

        elif 'rubl' in text or 'rub' in text:
            amount = float(''.join(filter(str.isdigit, text)))
            result = amount * rates['RUB']
            update.message.reply_text(f"{amount} RUB ≈ {round(result)} so'm")

        else:
            update.message.reply_text("valyuta bilan yozing: masalan, 100 USD yoki 150000 so'm")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(handle_message))
updater.start_polling()

# from pygrambot.updater import Updater
# from pygrambot.handlers import MessageHandler
# from pygrambot.types import Update
# from config import TOKEN


# def handle_message(update: Update):
#     if update.message.text:
#         update.message.reply_text(update.message.text)


# updater = Updater(TOKEN)
# updater.dispatcher.add_handler(MessageHandler(handle_message))

# updater.start_polling()