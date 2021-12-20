from conf.base_logger import logger
from urllib import error
from h1_creds import check_h1_credentials_exist
from h1_info import get_h1_programs, write_results_to_file, clean_companies_file
from conf.config import api_get_programs_endpoint
from h1_scrape import scrape_company
from h1_company_file import filter_company_file
from h1_search import get_word_file, get_all_spellings, search_h1_web_data
import sys


def prime_time_scrape(company_name, list_words):
    try:
        web_data = scrape_company(company_name)
        return search_h1_web_data(company_name, list_words, web_data)
    except error.HTTPError:
        logger.warning(f"HTTPError when scraping {company_name}")
    finally:
        pass


def main():
    h1_creds = check_h1_credentials_exist()
    if h1_creds is None:
        sys(exit())

    # Todo: Menu options to get H1 program info to write local file
    clean_companies_file()
    result = get_h1_programs(username=h1_creds.username,
                             token=h1_creds.access_token,
                             next_url=api_get_programs_endpoint)
    assert result is True
    # Todo: Menu options for scraping web after read of local file
    # words_list = get_all_spellings(get_word_file())
    # for c in filter_company_file():
    #     res = prime_time_scrape(c.name, words_list)
    #     if res is not None and len(res) > 0:
    #         print(res)


