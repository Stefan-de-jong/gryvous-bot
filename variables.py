import os
from dotenv import load_dotenv

load_dotenv()

_client_id=os.getenv('CLIENT_ID')
_client_secret=os.getenv('CLIENT_SECRET')
_password=os.getenv('BOT_PASSWORD')
_username=os.getenv('BOT_USERNAME')