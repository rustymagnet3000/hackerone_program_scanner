import os
import sys
from conf.base_logger import logger
from typing import NamedTuple


class H1creds(NamedTuple):
    """
      Acess Token required to send API requests to HackerOne
    """
    username: str
    access_token: str


def check_h1_credentials_exist() -> H1creds:
    """
    Check Hackerone Credentials exist as environment variables
    :return: NamedTuple of the h1_username, h1_api_token
    """
    if "VIRTUAL_ENV" in os.environ:
        logger.info(f'Running inside virtual environment')

    creds = H1creds(os.getenv('H1_USERNAME'), os.getenv('H1_API_TOKEN'))
    if creds.access_token is None or creds.username is None:
        logger.warning(f"Set the HackerOne env variables")
        sys.exit()

    logger.info(f"Found HackerOne Credentials")
    return creds
