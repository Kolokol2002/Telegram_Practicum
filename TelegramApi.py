import telegram
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = '454836837'

def send_message(message):

    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    return bot.send_message(chat_id=CHAT_ID, text=message)

send_message('Привет, я ботик, у меня баги')