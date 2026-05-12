import os
import sys

from src.exception import CustomException
from src.logger import logging


def create_directories(path_to_directories: list, verbose=True):

    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)

            if verbose:
                logging.info(f"Created directory at: {path}")

    except Exception as e:
        raise CustomException(e, sys)