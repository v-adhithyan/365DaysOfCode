import urllib2
from bs4 import BeautifulSoup

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