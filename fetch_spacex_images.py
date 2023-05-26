import requests
import argparse
from nasa_photo_api import cut_to_extension, make_images_dir, get_nasa_token


# def fetch_spacex_last_launch(url, images_path, nasa_token):
parser = argparse.ArgumentParser(
    description='Launch picture'
)
parser.add_argument('--Launch_ID', help='Input Launch ID')
args = parser.parse_args()
launch_ID = args.Launch_ID
print(launch_ID)
nasa_token = get_nasa_token()
if launch_ID:
    url_spacex = 'https://api.spacexdata.com/v5/launches/{0}'.format(launch_ID)
else:
    url_spacex = 'https://api.spacexdata.com/v5/launches/latest'
images_path = make_images_dir()
# payload = {"api_key": nasa_token}
response = requests.get(url_spacex)
response.raise_for_status()
pictures = response.json()['links']['flickr']['original']
for picture_number, picture in enumerate(pictures):
    response = requests.get(picture)
    filename = 'Spacex_{0}{1}'.format(picture_number, cut_to_extension(picture))
    with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
        file.write(response.content)
