from pygrambot.updater import Updater
from pygrambot.handlers import MessageHandler
from pygrambot.types import Update
from config import TOKEN


def handle_message(update: Update):
    if update.message.text:
        update.message.reply_text(update.message.text)


updater = Updater(TOKEN)
updater.dispatcher.add_handler(MessageHandler(handle_message))

updater.start_polling()