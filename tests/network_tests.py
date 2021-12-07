import pytest
from h1_scrape import h1_required_http_headers, scrape_company
from conf.config import (
    h1_dummy_local_endpoint,
    h1_web_endpoint
)
from urllib.request import urlopen, Request


class Test:

    company_name = 'coinbase'

    @pytest.fixture
    def urllib_h1_request(self):
        return Request(str(h1_web_endpoint + self.company_name), headers=h1_required_http_headers())

    def test_local_html_scrape(self):
        req = Request(h1_dummy_local_endpoint, headers=h1_required_http_headers())
        _content = urlopen(req).read()
        assert isinstance(_content, bytes)

    def test_h1_web_is_up(self, urllib_h1_request):
        with urlopen(urllib_h1_request) as f:
            assert f.read(50).decode('utf-8')   # read 50 bytes

    def test_h1_scrape_response_code(self, urllib_h1_request):
        with urlopen(urllib_h1_request) as f:
            assert f.status == 200

    def test_coinbase_returned_web_data(self, urllib_h1_request):
        res = scrape_company(self.company_name)
        print(res)
