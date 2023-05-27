import os
from dotenv import load_dotenv, find_dotenv
import telegram


load_dotenv(find_dotenv())
tg_token = os.environ.get("TG_TOKEN")
telegram_NASA_bot = telegram.Bot(token=tg_token)
# chat_id = telegram_NASA_bot.get_updates()[-1].message.chat_id
# telegram_NASA_bot.send_message(chat_id='@photo_nasa_channel', text="I'm sorry Dave I'm afraid I can't do that.")
telegram_NASA_bot.send_document(chat_id='@photo_nasa_channel', document=open('images/Spacex_0.jpg', 'rb'))
print(telegram_NASA_bot)