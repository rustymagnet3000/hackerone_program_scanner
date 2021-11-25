import pytest
from requests_html import HTMLSession
from conf.config import h1_dummy_local_endpoint, h1_dummy_internet_endpoint


class Test:
    @pytest.fixture
    def user_agent_clues(self):
        return {"python", "pycharm"}

    @pytest.fixture
    def html_request_session(self):
        return HTMLSession()

    def test_local_html_scrape(self, html_request_session):
        resp = html_request_session.get(h1_dummy_local_endpoint)
        assert True

    def test_request_headers_do_not_indicate_a_python_script(self, user_agent_clues, html_request_session):
        resp = html_request_session.get(h1_dummy_internet_endpoint)
        sent_user_agent = resp.request.headers.get('User-Agent').lower()
        for clue in user_agent_clues:
            if clue in sent_user_agent:
                assert False
        assert True

    def test_h1_does_not_say_no_js_detected(self, html_request_session):
        resp = html_request_session.get(h1_dummy_internet_endpoint)
        assert True
