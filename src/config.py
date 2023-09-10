from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

# Get env variables
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
API_LINK = os.environ.get('API_LINK')
