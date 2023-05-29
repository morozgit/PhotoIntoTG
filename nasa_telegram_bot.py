import os
from dotenv import load_dotenv, find_dotenv
import telegram
import random
import time
import argparse


parser = argparse.ArgumentParser(
    description='Send frequency'
)
parser.add_argument(
    '-t',
    '--time',
    help='Input minute',
    type=float,
    default=14400
    )
args = parser.parse_args()
seconds = args.time * 60

load_dotenv(find_dotenv())
tg_token = os.environ.get("TG_TOKEN")
telegram_NASA_bot = telegram.Bot(token=tg_token)
chat_id_tg = os.environ.get("CHAT_ID")
pictures_list = []
directory = 'images'
for address, dirs, picture in os.walk(directory):
    pictures_list.append(picture)
    # print(picture)
while True:
    random.shuffle(picture)
    telegram_NASA_bot.send_document(
        chat_id=chat_id_tg,
        document=open('{0}/{1}'.format(directory, picture[0]), 'rb')
        )
    time.sleep(seconds)