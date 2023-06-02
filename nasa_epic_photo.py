import requests
from nasa_photo_api import download_picture
import os
from dotenv import load_dotenv, find_dotenv


def main():
    load_dotenv(find_dotenv())
    nasa_token = os.environ.get("NASA_TOKEN")
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {"api_key": nasa_token}
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    nasa_epic_images_response = response.json()
    epic_images = []
    for nasa_epic_image in nasa_epic_images_response:
        images_data = nasa_epic_image['date'].partition(' ')[0].replace('-', '/')
        images_name = nasa_epic_image['image']
        archive_epic_images = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png'.format(images_data, images_name)
        epic_images.append(archive_epic_images)
    for image_epic_number, image_epic in enumerate(epic_images):
        download_picture(image_epic_number, image_epic)


if __name__ == '__main__':
    main()
