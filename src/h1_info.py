import requests
from config import H1Program, filename
import csv
from conf.base_logger import logger


def write_results_to_file(results: list):
    logger.info(f"Writings results {len(results)}")
    if len(results) == 0:
        logger.warning(f"No results found.")
    else:
        with open(filename, 'w', newline='') as result_file:  # overwrites any results that exist in the file
            csv_out = csv.writer(result_file)
            csv_out.writerow(['id', 'name', 'offers_bounties', 'triage_active'])
            for r in results:
                csv_out.writerow(r)
    return None


def get_h1_programs(username,
                    token,
                    endpoint: str,
                    h1_programs: list
                    ):
    headers = {
        'Accept': 'application/json'
    }

    resp = requests.get(
        url=endpoint,
        auth=(username, token),
        headers=headers
    )

    # check if page paginates. If so make a recursive call
    links = resp.json().get('links', {})
    next_url = links.get('next', None)
    h1_results = resp.json().get("data")

    # TODO: Remove comment
    # if next_url:
    #     logging.info(f'[*]H1 Programs found {len(h1_programs)}.\tPagination found: {next_url}')
    #     get_h1_programs(username, token, next_url, h1_programs)

    # at this point, you unwind the recursion. Iterating through all H1 Program with a for loop
    for p in h1_results:
        program_id = p.get('id')
        name = p.get('attributes').get('name')
        triage_active = p.get('attributes').get('triage_active')
        offers_bounties = p.get('attributes').get('offers_bounties')
        company = H1Program(program_id, name, offers_bounties, triage_active)
        h1_programs.append(company)
    return h1_programs
