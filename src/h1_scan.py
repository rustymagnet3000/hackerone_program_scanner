from conf.base_logger import logger
from conf.config import H1Program, filename, h1_web_endpoint
from csv import reader
from requests_html import HTMLSession


def open_file_of_companies():
    logger.info(f"Reading file")
    results = []
    with open(filename, 'r', newline='') as result_file_csv:
        csv_reader = reader(result_file_csv)
        for company in map(H1Program._make, csv_reader):
            results.append(company)
    return results


def read_company_file():
    comps_file = open_file_of_companies()
    if comps_file is None:
        logger.warning(f"Error reading report")
    filtered = filter(lambda c: c.offers_bounties == 'True' and c.triage_active == '', comps_file)
    for c in filtered:
        print(c)
    logger.info("Final RESULTS")
    scrape_company("Coinbase")


def scrape_company(company_name: str):
    logger.info("Scrape started RESULTS")
    headers = {
        'Accept-Encoding': 'identity',
        'content-type': 'text/html; charset=utf-8'
    }
    session = HTMLSession()
    resp = session.get(h1_web_endpoint + company_name)
    print(resp)
    # parse body of text for spelling mistakes

