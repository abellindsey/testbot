from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging


TOKEN = '824661485:AAE30eV44S8e8jd5LfsDZc-Rg9p0rqJjrug'

updater = Updater(TOKEN, use_context=True)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello mazafaka")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()