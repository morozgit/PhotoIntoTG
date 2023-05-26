import os
from dotenv import load_dotenv, find_dotenv

import requests



# def download_file(url, images_path):
#     filename = 'hubble{0}'.format(cut_to_extension(url))
#     response = requests.get(url)
#     response.raise_for_status()
#     with open('{0}/{1}'.format(images_path, filename), 'wb') as file:
#         file.write(response.content)





def main():
    load_dotenv(find_dotenv())
    nasa_token = os.environ.get("NASA_TOKEN")
    images_path = os.path.join(os.getcwd(), 'images')
    os.makedirs(images_path, exist_ok=True)
    # token = {"api_key": NASA_TOKEN}
    # url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # download_file(url, images_path)
    # url_spacex = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    # fetch_spacex_last_launch(url_spacex, images_path)

    # url_APOD = 'https://api.nasa.gov/planetary/apod'
    # start_date = datetime.datetime.today().strftime('%Y/%m/%d')
    # download_APOD(url_APOD, images_path, start_date)

    # url_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
    # get_nasa_epic(url_nasa_epic, images_path, token)


if __name__ == '__main__':
    main()
