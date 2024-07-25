from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMIN_ID = env.list('ADMIN_ID')
CHANNEL_ID = env.list('CHANNEL_ID', '-1001275637856')
# print(CHANNEL_ID)

# postgres
DB_USER = env.str('DB_USER')
DB_PASS = env.str('DB_PASS')
DB_NAME = env.str('DB_NAME')
DB_HOST = env.str('DB_HOST')

BASE_URL = env.str('BASE_URL')
