import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from tv import movies
from bse import bse_price
from nse import nse_price
from akshay_seth_analysis import  analysis as akseth
from add import add_stock

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
bse_handler = CommandHandler("bse", bse_price)
nse_handler = CommandHandler("nse", nse_price)
add_handler = CommandHandler("add", add_stock)
#akseth_handler = CommandHandler("akseth", akseth)

TOKEN = os.environ["TELEGRAM_TOKEN"]
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(movie_handler)
dispatcher.add_handler(bse_handler)
dispatcher.add_handler(nse_handler)
#dispatcher.add_handler(akseth_handler)
dispatcher.add_handler(add_handler)

updater.start_polling()