import logging
import pytest

@pytest.fixture(autouse=True, scope="session")
def configure_logging():
    logging.getLogger().setLevel(logging.INFO)


    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%H:%M:%S'
    )
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)