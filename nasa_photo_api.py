import os
from urllib.parse import urlparse


def make_images_dir():
    images_path = os.path.join(os.getcwd(), 'images')
    os.makedirs(images_path, exist_ok=True)


def cut_to_extension(url):
    piece_of_url = urlparse(url)
    piece_of_url_path = os.path.split(piece_of_url.path)
    extension = os.path.splitext(piece_of_url_path[1])
    return extension[1]
