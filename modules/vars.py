from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 29687224))
API_HASH = getenv("API_HASH", c543dbfe3007000fbecbd48c10731a55)
BOT_TOKEN = getenv("BOT_TOKEN", 6631189368:AAE2lhyuhmftTh0jt0Cs75oTXhKlMwlxRuw)
OWNER_ID = int(getenv("OWNER_ID", 6427042108))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6427042108 ").split()))
