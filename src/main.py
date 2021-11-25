import os
from h1_info import get_h1_programs, write_results_to_file
from conf.base_logger import logger
from src.config import api_get_programs_endpoint
from src.h1_scan import read_company_file


def main():
    if "VIRTUAL_ENV" in os.environ:
        logger.info(f'Running inside virtual environment')

    h1_username = os.getenv('H1_USERNAME')
    h1_api_token = os.getenv('H1_API_TOKEN')

    if h1_username is None or h1_api_token is None:
        logger.warning(f"Set the H1 env variables")
        return None

    read_company_file()

    programs = get_h1_programs(username=h1_username,
                               token=h1_api_token,
                               endpoint=api_get_programs_endpoint,
                               h1_programs=[])

    write_results_to_file(programs)
