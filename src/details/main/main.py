import logging
import time
import sys

from dotenv import load_dotenv
from details.app_facotry import AppFactory


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def start_app():
    logger = logging.getLogger(__name__)
    logger.info('Запускаю приложение')
    yana_id = '250798893'
    load_dotenv()
    cmd = AppFactory.create_notify_about_dota_match_command()

    while True:
        logger.info(f'Начинаю итерация для {yana_id}')
        cmd.execute(yana_id)
        time.sleep(10)
        logger.info(f'Заканчиваю итерация для {yana_id}')


if __name__ == "__main__":
    setup_logging()
    start_app()
