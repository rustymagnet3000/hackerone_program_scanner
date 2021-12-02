from conf.base_logger import logger
from conf.config import H1Program, filename, h1_web_endpoint
from csv import reader


def open_file_of_companies() -> list:
    logger.info(f"Opening Companies file")
    results = []
    with open(filename, 'r', newline='') as result_file_csv:
        csv_reader = reader(result_file_csv)
        for company in map(H1Program._make, csv_reader):
            results.append(company)
    return results


def read_company_file() -> list:
    """
    Filters a local file of companies using Hackerone. Filters on those who offer Bounties and are not Triaged by H1
    :return: list
    """
    comps_file = open_file_of_companies()
    if comps_file is None:
        logger.warning(f"Error reading report")
    filtered = filter(lambda c: c.offers_bounties == 'True' and c.triage_active == '', comps_file)
    logger.info("Finished reading Company File")
    return list(filtered)

