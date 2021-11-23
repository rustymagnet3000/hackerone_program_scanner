import logging
import os
import requests
from collections import namedtuple

H1Program = namedtuple('H1Program', ['id', 'name'])


def write_results_to_file(results: list):            # print(f'{program_id.rjust(8)}\t{name.rjust(30)}')
    with open('results.txt', 'a') as result_file:
        for i in results:
            result_file.write(f'{i.id},{i.name}\n')
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
    if next_url:
        logging.info(f'[*]H1 Programs found {len(h1_programs)}.\tPagination found: {next_url}')
        get_h1_programs(username, token, next_url, programs)

    # at this point, you unwind the recursion. Iterating through all H1 Program with a for loop
    for p in h1_results:
        program_id = p.get('id')
        name = p.get('attributes').get('name')
        company = H1Program(program_id, name)
        h1_programs.append(company)
    return programs


logging.getLogger().setLevel(logging.INFO)


def main():
    if "VIRTUAL_ENV" in os.environ:
        logging.info(f'[*]Running inside virtual environment')

    h1_username = os.getenv('H1_USERNAME')
    h1_api_token = os.getenv('H1_API_TOKEN')

    if h1_username is None or h1_api_token is None:
        logging.warning(f"[!]Set the H1 env variables")
        exit(99)

    programs = get_h1_programs(username=h1_username,
                      token=h1_api_token,
                      endpoint="https://api.hackerone.com/v1/hackers/programs",
                      h1_programs=[])

    write_results_to_file(programs)
