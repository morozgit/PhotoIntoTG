import requests
import argparse
from nasa_photo_api import download_pictures


def main():
    parser = argparse.ArgumentParser(
        description='Launch picture'
    )
    parser.add_argument(
        '-id',
        '--launch_id',
        help='Input Launch ID',
        default='latest'
        )
    args = parser.parse_args()
    launch_id = args.launch_id
    spacex_url = 'https://api.spacexdata.com/v5/launches/{0}'.format(launch_id)
    try:
        response = requests.get(spacex_url)
        response.raise_for_status()
        pictures = response.json()['links']['flickr']['original']
        for picture_number, picture in enumerate(pictures):
            download_pictures(picture_number, picture)
    except requests.exceptions.HTTPError:
        print('Photo didn`t do')


if __name__ == '__main__':
    main()
