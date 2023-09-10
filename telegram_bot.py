import requests
from config import TELEGRAM_TOKEN, CHAT_ID


def send_telegram_message(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"Telegram message sent successfully to chat ID {CHAT_ID}!")
        else:
            print(f"Failed to send Telegram message to chat ID {CHAT_ID}: {response.content}")
    except Exception as e:
        print(f"An error occurred while sending Telegram message to chat ID {CHAT_ID}: {e}")
