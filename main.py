import os
from dotenv import load_dotenv, find_dotenv
import datetime
import requests
from urllib.parse import urlparse


def download_file(url, images_path):
    filename = 'hubble{0}'.format(cut_to_extension(url))
    response = requests.get(url)
    response.raise_for_status()
    with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url, images_path):
    response = requests.get(url)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        response = requests.get(picture)
        filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))       
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)


def cut_to_extension(url):
    piece_of_url = urlparse(url)
    piece_of_url_path = os.path.split(piece_of_url.path)
    extension = os.path.splitext(piece_of_url_path[1])
    return extension[1]


def download_APOD(url, images_path, start_date):
    payload = {"api_key": "cZHYAr5rNUxpMhgz3FcbL2xeVshvbVAE51wTIgMz", "start_date" : start_date}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    nasa_response = response.json()
    images_list = []

    for piece_of_nasa_response in nasa_response:
        image_url = piece_of_nasa_response['hdurl']
        images_list.append(image_url)
    for image_number, image in enumerate(images_list):
        response = requests.get(image)
        filename = 'nasa_apod_{0}{1}'.format(image_number, cut_to_extension(image))       
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)


def get_nasa_epic(url, images_path, payload):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    nasa_epic_response = response.json()
    epic_images_list = []
    for piece_of_nasa_epic_response in nasa_epic_response:
        images_data = piece_of_nasa_epic_response['date'].partition(' ')[0].replace('-', '/')
        images_name = piece_of_nasa_epic_response['image']
        archive_epic_images = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png?api_key=DEMO_KEY'.format(images_data, images_name)
        epic_images_list.append(archive_epic_images)
    print(epic_images_list)
    for image_epic_number, image_epic in enumerate(epic_images_list):
        response = requests.get(image_epic)
        filename = 'nasa_apod_{0}{1}'.format(image_epic_number, cut_to_extension(image_epic))
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)


def main():
    load_dotenv(find_dotenv())
    NASA_TOKEN = os.environ.get("NASA_TOKEN")
    images_path = os.path.join(os.getcwd(), 'images')
    os.makedirs(images_path, exist_ok=True)
    payload = {"api_key": NASA_TOKEN}
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_file(url, images_path)
    url_spacex = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(url_spacex, images_path)

    url_APOD = 'https://api.nasa.gov/planetary/apod'
    start_date = datetime.datetime.today().strftime('%Y/%m/%d')
    download_APOD(url_APOD, images_path, start_date)

    url_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
    get_nasa_epic(url_nasa_epic, images_path, payload)


if __name__ == '__main__':
    main()
