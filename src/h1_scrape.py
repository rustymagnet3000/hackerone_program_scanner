from urllib.request import urlopen, Request
from conf.base_logger import logger
from conf.config import h1_web_endpoint


def h1_required_http_headers() -> str:
    return {
        'Accept': 'application/json, text/javascript',
        'User-Agent': 'Mozilla/5.0 Pseudo',
        'X-Requested-With': 'XMLHttpRequest'
    }


def build_h1_request(h1_company_name) -> Request:
    return Request(str(h1_web_endpoint + h1_company_name), headers=h1_required_http_headers())


def scrape_company(company_name: str) -> :
    logger.info(f"Scrape started for {company_name}")
    req = build_h1_request(company_name)
    with urlopen(req) as f:
        return f.read().decode('utf-8')  # read 50 bytes
