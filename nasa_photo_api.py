import os
from urllib.parse import urlparse
from dotenv import load_dotenv, find_dotenv


def get_nasa_token():
    load_dotenv(find_dotenv())
    nasa_token = os.environ.get("NASA_TOKEN")
    return nasa_token


def make_images_dir():
    images_path = os.path.join(os.getcwd(), 'images')
    os.makedirs(images_path, exist_ok=True)
    return images_path


def cut_to_extension(url):
    piece_of_url = urlparse(url)
    piece_of_url_path = os.path.split(piece_of_url.path)
    extension = os.path.splitext(piece_of_url_path[1])
    return extension[1]
