import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from tv import movies
from share_price import get_quote

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Adhithyan's Bot says Hai !")



def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


setup_logger()

start_handler = CommandHandler('start', start)
movie_handler = CommandHandler("movies", movies)
share_price_handler = CommandHandler("shareprice", get_quote)

TOKEN = os.environ["TELEGRAM_TOKEN"]
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(movie_handler)
dispatcher.add_handler(share_price_handler)

updater.start_polling()