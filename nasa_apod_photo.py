import requests
from nasa_photo_api import cut_to_extension, make_images_dir


def download_APOD(url, start_date, nasa_token):
    images_path = make_images_dir()
    payload = {"api_key": nasa_token, "start_date": start_date}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    nasa_response = response.json()
    images_list = []

    for piece_of_nasa_response in nasa_response:
        image_url = piece_of_nasa_response['hdurl']
        images_list.append(image_url)
    for image_number, image in enumerate(images_list):
        response = requests.get(image)
        filename = 'nasa_apod_{0}{1}'.format(image_number, cut_to_extension(image))       
        with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
            file.write(response.content)