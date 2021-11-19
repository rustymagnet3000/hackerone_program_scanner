import logging
import os
import requests


def create_h1_request(username, token):
    headers = {
        'Accept': 'application/json'
    }

    r = requests.get(
        'https://api.hackerone.com/v1/hackers/payments/earnings',
        auth=(username, token),
        headers=headers
    )
    print(r.json())
    return None


logging.getLogger().setLevel(logging.DEBUG)

if __name__ == '__main__':
    if "VIRTUAL_ENV" in os.environ:
        logging.info(f'[*]Running inside virtual environment')

    h1_username = os.getenv('H1_USERNAME')
    h1_api_token = os.environ.get('H1_API_TOKEN', None)

    if h1_username is None or h1_api_token is None:
        logging.warn(f"[!]Set the H1 env variables")
        exit(99)

    create_h1_request(username=h1_username, token=h1_api_token)
