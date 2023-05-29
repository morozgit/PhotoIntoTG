import requests
from nasa_photo_api import cut_to_extension, make_images_dir, get_nasa_token


nasa_token = get_nasa_token()
url_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
images_path = make_images_dir()
payload = {"api_key": nasa_token}
response = requests.get(url_nasa_epic, params=payload)
response.raise_for_status()
nasa_epic_response = response.json()
epic_images_list = []
for piece_of_nasa_epic_response in nasa_epic_response:
    images_data = piece_of_nasa_epic_response['date'].partition(' ')[0].replace('-', '/')
    images_name = piece_of_nasa_epic_response['image']
    archive_epic_images = 'https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png'.format(images_data, images_name)
    epic_images_list.append(archive_epic_images)
for image_epic_number, image_epic in enumerate(epic_images_list):
    response = requests.get(image_epic, params=payload)
    filename = 'nasa_epic_{0}{1}'.format(image_epic_number, cut_to_extension(image_epic))
    with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
        file.write(response.content)