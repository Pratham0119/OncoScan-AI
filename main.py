import sys
from src.logger import logging
from src.exception import CustomException


if __name__ == "__main__":
    logging.info("Logging has started successfully.")

    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero error occurred.")
        raise CustomException(e, sys)