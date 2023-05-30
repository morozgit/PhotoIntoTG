import os
from dotenv import load_dotenv, find_dotenv
import telegram
import random
import time
import argparse


def main():
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
    telegram_nasa_bot = telegram.Bot(token=tg_token)
    chat_id_tg = os.environ.get("TG_CHAT_ID")
    pictures = []
    directory = 'images'
    for address, dirs, picture in os.walk(directory):
        pictures.append(picture)
    while True:
        random.shuffle(picture)
        with open('{0}/{1}'.format(directory, picture[0]), 'rb') as image:
            telegram_nasa_bot.send_document(chat_id_tg, image)
        time.sleep(seconds)


if __name__ == '__main__':
    main()