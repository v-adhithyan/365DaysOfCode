#!/home/adhi/.pyenv/shims/python3
import ctypes
import os
import platform
import random
import shutil
from collections import namedtuple
from tempfile import NamedTemporaryFile
from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup

wallpaper = namedtuple("wallpaper", "src title")
URL = "https://bing.wallpaper.pics/"


def get_image_for_windows(image):
    old_file = image.name
    new_file = old_file + ".png"
    shutil.copy(old_file, new_file)
    return new_file


def save_image_to_pictures(image):
    n = random.randint(1, 1000)
    os.system(f"rm ~/Pictures/py_daily_wallpaper*.png")
    new_file = os.path.expanduser(f"~/Pictures/py_daily_wallpaper_{n}.png")
    shutil.copy(image.name, new_file)
    return new_file


def cleanup(f):
    pass


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
    system_os = platform.system().lower()

    if system_os == "linux":
        os.system(
            "/usr/bin/gsettings set org.gnome.desktop.background picture-uri {}".format(img.name))
    elif system_os == "darwin":  # mac
        mac_image = save_image_to_pictures(img)
        os.system(
            "osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{}\"'".format(mac_image))
    elif system_os == "windows":
        image = get_image_for_windows(img)
        SET_WALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(
            SET_WALLPAPER, 0, image, 3)
        cleanup(image)
    else:
        raise OSError("Unsupported OS.")


set_wallpaper()
