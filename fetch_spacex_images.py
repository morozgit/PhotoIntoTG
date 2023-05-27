import requests
import argparse
from nasa_photo_api import cut_to_extension, make_images_dir, get_nasa_token


parser = argparse.ArgumentParser(
    description='Launch picture'
)
parser.add_argument('-lid', '--Launch_ID', help='Input Launch ID')
args = parser.parse_args()
launch_ID = args.Launch_ID
nasa_token = get_nasa_token()
if launch_ID:
    url_spacex = 'https://api.spacexdata.com/v5/launches/{0}'.format(launch_ID)
else:
    url_spacex = 'https://api.spacexdata.com/v3/launches/latest'
images_path = make_images_dir()
try:
    response = requests.get(url_spacex)
    response.raise_for_status()
    pictures = response.json()['links']['flickr']['original']
    for picture_number, picture in enumerate(pictures):
        response = requests.get(picture)
        filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)
except requests.exceptions.HTTPError:
    print('Photo didn`t do')
