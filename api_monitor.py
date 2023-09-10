import requests
from telegram_bot import send_telegram_message
from api_logger import log_api_status
from config import API_LINK


def check_api():
    try:
        response = requests.get(API_LINK)
        if response.status_code != 200:
            log_message = f"API is down! Status code: {response.status_code}"
            log_api_status(log_message, "error")
            send_telegram_message(log_message)
        else:
            log_message = "API is up and running!"
            log_api_status(log_message, "info")
            print(log_message)
    except Exception as e:
        log_message = f"An error occurred while checking API: {e}"
        log_api_status(log_message, "error")
        send_telegram_message(log_message)
