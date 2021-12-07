from urllib.request import urlopen, Request
from conf.base_logger import logger
from conf.config import h1_web_endpoint


def h1_required_http_headers():
    return {
        'Accept': 'application/json, text/javascript',
        'User-Agent': 'Mozilla/5.0 Pseudo',
        'X-Requested-With': 'XMLHttpRequest'
    }


def build_h1_request(h1_company_name):
    return Request(str(h1_web_endpoint + h1_company_name), headers=h1_required_http_headers())


def scrape_company(company_name: str):
    """
    :param company_name:used to build the request URL
    :return: long string with all content from website
    """
    logger.info(f"{company_name}\tscrape started")
    req = build_h1_request(company_name)
    with urlopen(req) as f:
        return f.read().decode('utf-8')
