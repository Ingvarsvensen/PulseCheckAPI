import logging

# Configure logging
logging.basicConfig(filename='api_status.log', level=logging.INFO)


def log_api_status(message, status):
    if status == "error":
        logging.error(message)
    else:
        logging.info(message)
