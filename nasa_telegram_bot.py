import os
from dotenv import load_dotenv, find_dotenv
import telegram
import random
import time


load_dotenv(find_dotenv())
tg_token = os.environ.get("TG_TOKEN")
telegram_NASA_bot = telegram.Bot(token=tg_token)
# chat_id = telegram_NASA_bot.get_updates()[-1].message.chat_id
# telegram_NASA_bot.send_message(chat_id='@photo_nasa_channel', text="I'm sorry Dave I'm afraid I can't do that.")
pictures_list = []
directory = 'images'
for address, dirs, picture in os.walk(directory):
    pictures_list.append(picture)
    # print(picture)
while True:
    random.shuffle(picture)
    telegram_NASA_bot.send_document(chat_id='@photo_nasa_channel', document=open('{0}/{1}'.format(directory, picture[0]), 'rb'))
    time.sleep(60)
print(pictures_list)