import os
from h1_info import get_h1_programs, write_results_to_file
from src.base_logger import logger


def main():
    if "VIRTUAL_ENV" in os.environ:
        logger.info(f'Running inside virtual environment')

    h1_username = os.getenv('H1_USERNAME')
    h1_api_token = os.getenv('H1_API_TOKEN')

    if h1_username is None or h1_api_token is None:
        logger.warning(f"Set the H1 env variables")
        exit(99)

    programs = get_h1_programs(username=h1_username,
                               token=h1_api_token,
                               endpoint="https://api.hackerone.com/v1/hackers/programs",
                               h1_programs=[])

    write_results_to_file(programs)
