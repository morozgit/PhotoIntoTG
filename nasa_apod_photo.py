import argparse
import requests
import os
from dotenv import load_dotenv, find_dotenv
from nasa_photo_api import download_picture


def main():
    parser = argparse.ArgumentParser(
        description='Astronomy Picture of the Day'
    )
    parser.add_argument('date_start', help='Input date YYYY-MM-DD')
    args = parser.parse_args()
    load_dotenv(find_dotenv())
    nasa_token = os.environ.get("NASA_TOKEN")
    start_date = args.date_start
    apod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {"api_key": nasa_token, "start_date": start_date}
    response = requests.get(apod_url, params=payload)
    response.raise_for_status()
    nasa_response = response.json()
    images = []
    for image_url in nasa_response:
        try:
            image_url = image_url['hdurl']
            images.append(image_url)
        except KeyError:
            print('Images downloading')

    for image_number, image in enumerate(images):
        download_picture(image_number, image)


if __name__ == '__main__':
    main()
