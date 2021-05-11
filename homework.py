import os
import time

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
token = os.getenv('Token')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
number_from = os.getenv('NUMBER_FROM')
number_to = os.getenv('NUMBER_to')

def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': '5.130',
        'access_token': token,
        'fields': 'online'
    }
    check = requests.post('https://api.vk.com/method/users.get', params)
    check_online = check.json()['response']
    return check_online[0]['online']  # Верните статус пользователя в ВК

client = Client(account_sid, auth_token)

def sms_sender(sms_text):
    message = client.messages \
        .create(
        body=sms_text,
        from_=number_from,
        to=number_to
    )
    return message.sid  # Верните sid отправленного сообщения из Twilio

# online = "166506281"
# offline = "192479170"
# print(get_status(online))

if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
