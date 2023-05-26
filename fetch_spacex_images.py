import requests
from main import cut_to_extension


def fetch_spacex_last_launch(url, images_path):
    response = requests.get(url)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        response = requests.get(picture)
        filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)
