import json

import requests

from data.config_reader import BASE_URL


# The user registers through telegram
async def register_user(telegram_id, username, full_name, nickname, phone_number):
    url = f"{BASE_URL}/user/create/"
    data = {
        "telegram_id": telegram_id,
        "username": username,
        "full_name": full_name,
        "nickname": nickname,
        "phone_number": phone_number
    }
    response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
    return response.status_code


#  Get user by telegram id
async def get_me(telegram_id):
    url = f"{BASE_URL}/user/me/{telegram_id}/"
    response = requests.get(url)
    data = json.loads(response.text)
    return {'data': data, 'status_code': response.status_code}
