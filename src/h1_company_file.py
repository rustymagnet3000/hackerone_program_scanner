from conf.base_logger import logger
from conf.config import H1Program, filename, h1_web_endpoint
from csv import reader


def open_file_of_companies():
    """
    Open local file that includes Hackerone:  id,name,offers_bounties,triage_active
    :return: list
    """
    logger.info(f"Attempting to open {filename}")
    with open(filename, 'r', newline='') as result_file_csv:
        csv_reader = reader(result_file_csv)
        return [company for company in map(H1Program._make, csv_reader)]


def tidy(h1: H1Program):
    """
    Dormant filter use to focus search on H1 Companies who are not H1 Triaged and Pay Rewards
    :return: Bool
    """
    # if h1.offers_bounties == 'False' or h1.offers_bounties == '':
    #     return False
    if h1.triage_active == 'True':
        return False
    return True


def filter_company_file():
    """
    Filters local file of companies into List of NamedTuples.
    Filters on those who offer Bounties and are not Triaged by H1
    :return: list
    """
    companies = open_file_of_companies()
    if companies is None or len(companies) == 0:
        logger.warning(f"Error reading report")
        return None
    # commented out filter as barely any companies meet the criteria
    filtered_list = list(filter(tidy, companies))
    logger.debug(f"Finished reading Company File. Found {len(companies)} companies")
    return companies

