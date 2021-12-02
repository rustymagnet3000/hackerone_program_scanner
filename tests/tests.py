import pytest
from conf.config import (
    h1_dummy_local_endpoint,
    h1_web_endpoint
)
from urllib.request import urlopen, Request


class Test:

    @pytest.fixture
    def http_headers(self):
        return {
            'Accept': 'application/json, text/javascript',
            'User-Agent': 'Mozilla/5.0 Pseudo',
            'X-Requested-With': 'XMLHttpRequest'
        }

    @pytest.fixture
    def h1_program_path(self):
        return 'coinbase'

    @pytest.fixture
    def urllib_h1_request(self, http_headers, h1_program_path):
        return Request(str(h1_web_endpoint + h1_program_path), headers=http_headers)

    def test_local_html_scrape(self, http_headers):
        req = Request(h1_dummy_local_endpoint, headers=http_headers)
        _content = urlopen(req).read()
        assert isinstance(_content, bytes)

    def test_h1_web_is_up(self, urllib_h1_request):
        with urlopen(urllib_h1_request) as f:
            assert f.read(50).decode('utf-8')   # read 50 bytes

    def test_h1_scrape_response_code(self, urllib_h1_request):
        with urlopen(urllib_h1_request) as f:
            assert f.status == 200

    def test_h1_scrape_response_code(self, urllib_h1_request):
        with urlopen(urllib_h1_request) as f:
            assert f.status == 200