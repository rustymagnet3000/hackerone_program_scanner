from h1_creds import check_h1_credentials_exist
from h1_info import get_h1_programs, write_results_to_file
from conf.base_logger import logger
from conf.config import api_get_programs_endpoint
from h1_scrape import scrape_company
from h1_open_company_file import read_company_file
from h1_search import get_word_file, get_all_spellings, search_h1_web_data


def print_gen(results_gen):
    return [r for r in results_gen if len(r) > 0]


def prime_time_scrape(company_name, words_g):
    web_data = scrape_company(company_name)
    res_gen = search_h1_web_data(company_name, words_g, web_data)
    print(print_gen(res_gen))


def main():
    h1_creds = check_h1_credentials_exist()

    # Todo: Menu options to get H1 program info OR read data from local file
    # programs = get_h1_programs(username=h1_creds.username,
    #                            token=h1_creds.access_token,
    #                            endpoint=api_get_programs_endpoint,
    #                            h1_programs=[])
    # write_results_to_file(programs)
    words_gen = get_all_spellings(get_word_file())
    for c in read_company_file():
        prime_time_scrape(c.name, words_gen)
