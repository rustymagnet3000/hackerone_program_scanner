import json
import logging
import os
import requests


def create_h1_request(username, token, endpoint: str):
    headers = {
        'Accept': 'application/json'
    }

    resp = requests.get(
        url=endpoint,
        auth=(username, token),
        headers=headers
    )

    # check if page paginates, recursive call
    links = resp.json().get('links', {})
    next_url = links.get('next', None)
    if next_url:
        logging.debug(f'[*]Pagination found.. inside virtual environment')
        create_h1_request(username, token, next_url)

    print("ending here")
    return None


logging.getLogger().setLevel(logging.DEBUG)

if __name__ == '__main__':
    if "VIRTUAL_ENV" in os.environ:
        logging.info(f'[*]Running inside virtual environment')

    h1_username = os.getenv('H1_USERNAME')
    h1_api_token = os.getenv('H1_API_TOKEN')

    if h1_username is None or h1_api_token is None:
        logging.warning(f"[!]Set the H1 env variables")
        exit(99)

    create_h1_request(username=h1_username,
                      token=h1_api_token,
                      endpoint="https://api.hackerone.com/v1/hackers/programs")
