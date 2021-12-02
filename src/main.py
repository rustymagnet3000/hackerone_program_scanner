from h1_creds import check_h1_credentials_exist
from h1_info import get_h1_programs, write_results_to_file
from conf.base_logger import logger
from conf.config import api_get_programs_endpoint
from h1_scrape import read_company_file
from h1_search import get_word_file, get_word_objects_to_search, search_h1_program_notes_for_misspellings


def main():
    h1_creds = check_h1_credentials_exist()

    # Todo: next to fix this step so it returns the scraped data
    read_company_file()

    programs = get_h1_programs(username=h1_creds.username,
                               token=h1_creds.access_token,
                               endpoint=api_get_programs_endpoint,
                               h1_programs=[])

    write_results_to_file(programs)

    words_dict = get_word_file()

    word_objs = get_word_objects_to_search(words_dict)

    results = search_h1_program_notes_for_misspellings(company_name, dummy_text, word_objs)

    logger.info(f"Final results:\n\t{results}")
