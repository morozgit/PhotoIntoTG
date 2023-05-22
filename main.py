import os
import requests


def download_file(url, images_path):
    filename = 'hubble.jpeg'
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
        filename = 'Spacex_{0}.jpeg'.format(picture_number)
        
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)


def main():
    images_path = os.path.join(os.getcwd(), 'images')
    os.makedirs(images_path, exist_ok=True)
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download_file(url, images_path)
    url_spacex = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    fetch_spacex_last_launch(url_spacex, images_path)


if __name__ == '__main__':
    main()
