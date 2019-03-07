#!/home/adhi/.pyenv/shims/python3
import os
import random
from collections import namedtuple
from tempfile import NamedTemporaryFile
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

wallpaper = namedtuple("wallpaper", "src title")
URL = "https://bing.wallpaper.pics/"


def pick_a_photo():
    data = requests.get(URL)
    soup = BeautifulSoup(data.content, "html.parser")
    photos = soup.find("div", {"id": "photos"}).find_all("img")
    photo = random.choice(photos)
    return wallpaper(src=photo["src"], title=photo["title"])


def set_wallpaper():
    photo = pick_a_photo()
    img = NamedTemporaryFile(delete=False)
    urlretrieve(photo.src, img.name)
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri {}".format(img.name))


set_wallpaper()
