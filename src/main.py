from h1_creds import check_h1_credentials_exist
from h1_info import get_h1_programs, write_results_to_file
from conf.base_logger import logger
from conf.config import api_get_programs_endpoint
from h1_scrape import scrape_company
from h1_open_company_file import read_company_file
from h1_search import get_word_file, get_all_spellings, search_h1_web_data


def main():
    h1_creds = check_h1_credentials_exist()

    # Todo: Menu options to get H1 program info OR read data from local file
    # programs = get_h1_programs(username=h1_creds.username,
    #                            token=h1_creds.access_token,
    #                            endpoint=api_get_programs_endpoint,
    #                            h1_programs=[])
    # write_results_to_file(programs)

    # targeted_h1_companies = read_company_file()
    # for t in targeted_h1_companies:
    company_name = 'coinbase'
    web_data = scrape_company(company_name)
    words_dict = get_word_file()
    words_gen = get_all_spellings(words_dict)
    results = search_h1_web_data(company_name, words_gen, web_data)
    logger.info(f"Results:")
    for r in results:
        logger.info(f"\t{r}")
