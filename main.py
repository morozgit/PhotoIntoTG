import os
import requests


def download_file(url, images_path):
    filename = 'hubble.jpeg'
    os.makedirs(images_path, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
        file.write(response.content)


def main():
    # url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # images_path = os.path.join(os.getcwd(), 'images')
    # download_file(url, images_path)
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    print(response.json()['links']['flickr']['original'])


if __name__ == '__main__':
    main()
