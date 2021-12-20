import requests
from conf.config import H1Program, filename, api_get_programs_endpoint
import csv
from conf.base_logger import logger
import re
import os.path

hostname_regex = re.compile("[^a-zA-Z]", flags=re.A)


def clean_companies_file():
    try:
        os.remove(filename)
        logger.info(f"Removed existing Company file{filename}")
    except FileNotFoundError as e:
        logger.debug(f"{filename}.\tno such file or directory")
    else:
        logger.warning(f"unhandled error removing {filename}.")
        pass


def write_results_to_file(results: list):
    logger.debug(f"Writing more results to {filename}")
    if len(results) == 0 or results is None:
        logger.warning(f"No results found.")
        return False

    with open(filename, 'w', newline='') as result_file:  # overwrites any results that exist in the file
        csv_out = csv.writer(result_file)
        for r in results:
            csv_out.writerow(r)
    return True


def send_request(username, token, endpoint):
    headers = {
        'Accept': 'application/json'
    }

    return requests.get(
        url=endpoint,
        auth=(username, token),
        headers=headers
    )


def get_h1_programs(username, token, next_url, limit_results=False):
    """
    When checking for a valid hostname, code ALWAYS return a hostname to keep downstream code cleaner
    :param limit_results: Optional parameter for unit tests
    :param next_url: URL of a paginated page
    :param username: H1 username
    :param token: H1 API token ( Hacker Token not Company Token )
    :return: List
    """
    resp = send_request(username, token, next_url)
    # check if page paginates. If so make a recursive call
    links = resp.json().get('links', {})
    next_url = links.get('next', None)
    h1_results = resp.json().get("data")

    if next_url and limit_results is False:
        logger.info(f'Following pagination: {next_url}')
        get_h1_programs(username, token, next_url)

    # Unwind recursion. Iterating through all H1 Program with a for loop
    return write_results_to_file([H1Program(p.get('id'),
                                            re.sub(hostname_regex, '', p.get('attributes').get('name')).lower(),
                                            p.get('attributes').get('triage_active'),
                                            p.get('attributes').get('offers_bounties'))
                                  for p in h1_results])
