from src.base_logger import logger
from config import H1Program, filename
from csv import reader


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
