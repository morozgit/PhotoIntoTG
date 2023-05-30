import os
from urllib.parse import urlparse
import requests


def make_images_dir():
    images_path = os.path.join(os.getcwd(), 'images')
    os.makedirs(images_path, exist_ok=True)
    return images_path


def cut_to_extension(url):
    piece_of_url = urlparse(url)
    piece_of_url_path = os.path.split(piece_of_url.path)
    extension = os.path.splitext(piece_of_url_path[1])
    return extension[1]


def download_pictures(picture_number, picture):
    response = requests.get(picture)
    response.raise_for_status()
    filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))
    with open('{0}/{1}'.format(make_images_dir(), filename), 'wb') as file:
        file.write(response.content)


    