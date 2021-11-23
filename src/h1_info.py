import requests
from collections import namedtuple

H1Program = namedtuple('H1Program', ['id', 'name'])


def write_results_to_file(results: list):
    from src.base_logger import logger
    logger.info(f"Writings results {len(results)}")
    # overwrites any results that exist in the file
    if len(results):
        logger.warning(f"Writings results {len(results)}")
    with open('results.txt', 'w', newline='\n') as result_file:
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

    # TODO: Remove comment
    # if next_url:
    #     logging.info(f'[*]H1 Programs found {len(h1_programs)}.\tPagination found: {next_url}')
    #     get_h1_programs(username, token, next_url, h1_programs)

    # at this point, you unwind the recursion. Iterating through all H1 Program with a for loop
    for p in h1_results:
        program_id = p.get('id')
        name = p.get('attributes').get('name')
        company = H1Program(program_id, name)
        h1_programs.append(company)
    return h1_programs
