import os
from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from bs4 import BeautifulSoup
import urllib2

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Adhithyan's Bot says Hai !")

def movies(bot, update):
    url = "https://timesofindia.indiatimes.com/tv/tvmoviefinder?languages=English,Tamil,Telugu,Malayalam,Kannada"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    movies = soup.find_all('div', attrs={'class': 'tvmovie-img'})

    title = "movie-title"
    genre  = "movie-genere"
    channel = "movie-channel"

    reply = ""
    for movie in movies:
        #movie = BeautifulSoup(m, "html.parser")
        movie_name = "*" + movie.find("span", attrs={'class': title}).text + "*" + "\n"
        movie_genre = "_" + movie.find("span", attrs={'class': genre}).text + "_" + "\n"
        movie_channel = movie.find("span", attrs={'class': channel}).text + "\n\n\n\n"

        reply  = "".join([reply, movie_name, movie_genre, movie_channel])

    bot.send_message(chat_id=update.message.chat_id, text=reply, parse_mode="Markdown")

def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

setup_logger()

TOKEN = os.environ["TELEGRAM_TOKEN"]

start_handler = CommandHandler('start', start)
movie_handler = CommandHandler("movies", movies)
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)
dispatcher.add_handler(movie_handler)

updater.start_polling()