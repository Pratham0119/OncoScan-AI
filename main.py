from src.logger import logging
from src.utils.common import create_directories


if __name__ == "__main__":

    logging.info("Creating test directories")

    create_directories(
        [
            "artifacts/data_ingestion",
            "artifacts/model_trainer"
        ]
    )

    logging.info("Directories created successfully")