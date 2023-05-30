import requests
import argparse
from nasa_photo_api import cut_to_extension, make_images_dir


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
images_path = make_images_dir()
try:
    response = requests.get(spacex_url)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        response = requests.get(picture)
        filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)
except requests.exceptions.HTTPError:
    print('Photo didn`t do')