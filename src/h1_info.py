import requests
from conf.config import H1Program, filename, api_get_programs_endpoint
import csv
from conf.base_logger import logger


def write_results_to_file(results: list):
    logger.info(f"Writings results {len(results)}")
    if len(results) == 0 or results is None:
        logger.warning(f"No results found.")
        return False
    elif results is None:
        logger.warning(f"Sent an empty / None results list")
        return False

    with open(filename, 'w', newline='') as result_file:  # overwrites any results that exist in the file
        csv_out = csv.writer(result_file)
        csv_out.writerow(['id', 'name', 'offers_bounties', 'triage_active'])
        for r in results:
            csv_out.writerow(r)
    return True


def send_request(username, token):
    headers = {
        'Accept': 'application/json'
    }

    return requests.get(
        url=api_get_programs_endpoint,
        auth=(username, token),
        headers=headers
    )


def get_h1_programs(username, token):
    """

    :param username:
    :param token:
    :return: List
    """
    resp = send_request(username, token)
    # check if page paginates. If so make a recursive call
    links = resp.json().get('links', {})
    next_url = links.get('next', None)
    h1_results = resp.json().get("data")

    # TODO: Remove comment
    # if next_url:
    #     logging.info(f'[*]H1 Programs found {len(h1_programs)}.\tPagination found: {next_url}')
    #     get_h1_programs(username, token, next_url, h1_programs)

    # at this point, you unwind the recursion. Iterating through all H1 Program with a for loop
    return [H1Program(p.get('id'),
                      p.get('attributes').get('name'),
                      p.get('attributes').get('triage_active'),
                      p.get('attributes').get('offers_bounties')) for p in h1_results]
