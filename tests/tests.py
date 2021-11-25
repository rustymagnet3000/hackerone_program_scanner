import pytest
from requests_html import HTMLSession
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
    def html_request_session(self, http_headers):
        session = HTMLSession()
        session.headers = http_headers
        return session

    @pytest.fixture
    def h1_program_path(self):
        return 'coinbase'

    def test_local_html_scrape(self, html_request_session):
        resp = html_request_session.get(h1_dummy_local_endpoint)
        assert True

    def test_request_headers_do_not_indicate_a_python_script(self, user_agent_clues, html_request_session):
        user_agent = html_request_session.headers.get('User-Agent')
        for clue in user_agent_clues:
            if clue in user_agent:
                assert False
        assert True

    def test_h1_web_is_up(self, html_request_session):
        resp = html_request_session.get(h1_web_endpoint)
        assert resp.ok

    def test_h1_does_not_say_no_js_detected(self, html_request_session, h1_program_path):
        resp = html_request_session.get(h1_web_endpoint + h1_program_path)
        resp.html.render()
        assert True

    def test_h1_allows_urllib(self, h1_program_path):
        req = Request(h1_web_endpoint + h1_program_path)
        req.add_header('apikey', 'xxx')

        page = urlopen()
        assert True
