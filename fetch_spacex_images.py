import requests
from nasa_photo_api import cut_to_extension


def fetch_spacex_last_launch(url, images_path, nasa_token):
    payload = {"api_key": nasa_token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        response = requests.get(picture)
        filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)
