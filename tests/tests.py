import pytest
from conf.config import (
    h1_dummy_local_endpoint,
    h1_dummy_internet_endpoint,
    h1_web_endpoint
)
from urllib.request import urlopen, Request


class Test:
    @pytest.fixture
    def user_agent_clues(self):
        return {"python", "pycharm"}

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
        content = urlopen(req).read()
        assert True

    def test_h1_web_is_up(self, urllib_h1_request):
        content = urlopen(urllib_h1_request).read()
        assert content is not None

    def test_h1_allows_urllib(self, urllib_h1_request, http_headers):
        content = urlopen(urllib_h1_request).read()
        html_bytes = content.read()
        assert True
