import argparse
import requests
from nasa_photo_api import cut_to_extension, make_images_dir, get_nasa_token


parser = argparse.ArgumentParser(
    description='Astronomy Picture of the Day'
)
parser.add_argument('date_start', help='Input date YYYY-MM-DD')
args = parser.parse_args()
nasa_token = get_nasa_token()
start_date = args.date_start
apod_url = 'https://api.nasa.gov/planetary/apod'
images_path = make_images_dir()
payload = {"api_key": nasa_token, "start_date": start_date}
response = requests.get(apod_url, params=payload)
response.raise_for_status()
nasa_response = response.json()
images = []
for piece_of_nasa_response in nasa_response:
    image_url = piece_of_nasa_response['hdurl']
    images.append(image_url)

for image_number, image in enumerate(images):
    response = requests.get(image)
    filename = 'nasa_apod_{0}{1}'.format(image_number, cut_to_extension(image))       
    with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
        file.write(response.content)