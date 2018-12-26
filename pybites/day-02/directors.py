import copy
import csv
import os
from collections import defaultdict, namedtuple
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movie_set = set()
    with open(MOVIE_DATA) as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = row['movie_title']
            year = row['title_year'].strip()
            if len(year) == 0 or (len(year) == 4 and int(year) < MIN_YEAR):
                continue
            year = int(year)
            score = float(row['imdb_score'].strip())
            director = row['director_name'].strip()
            movie_set.add((director, Movie(title, year, score)))

    movie_dict = defaultdict()

    for movie in movie_set:
        movie_list = copy.deepcopy(movie_dict.get(movie[0], []))
        movie_list.append(movie[1])
        movie_dict[movie[0]] = movie_list

    return movie_dict


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    total_score = float(0)
    for movie in movies:
        total_score += movie.score
    mean_score = total_score / len(movies)
    return round(mean_score, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    average_scores = [(director, calc_mean_score(movies)) for director, movies in directors.items() if
                      len(movies) >= MIN_MOVIES]
    # https://jeffknupp.com/blog/2018/12/13/how-to-do-just-about-anything-with-python-lists/
    return sorted(average_scores, key=lambda score: score[1], reverse=True)
