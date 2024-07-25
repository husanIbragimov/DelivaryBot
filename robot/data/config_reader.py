import os

from dotenv import load_dotenv  # pip install python-dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID').split(', ')
CHANNEL_ID = os.getenv('CHANNEL_ID', '-1001275637856').split(', ')
BASE_URL = os.getenv('BASE_URL', 'http://localhost:8000')
# print(CHANNEL_ID)

# postgres
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')
DB_HOST = os.getenv('DB_HOST')
