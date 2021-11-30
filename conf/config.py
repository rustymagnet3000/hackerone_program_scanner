from typing import NamedTuple

filename = '../companies.txt'
api_get_programs_endpoint = "https://api.hackerone.com/v1/hackers/programs"
h1_web_endpoint = "https://hackerone.com/"
h1_dummy_local_endpoint = "http://127.0.0.1:8080"
h1_dummy_internet_endpoint = "https://httpbin.org"


class H1Program(NamedTuple):
    """
      blueprint for H1Program
    """
    id: int
    name: str
    offers_bounties: bool
    triage_active: bool
