import pytest
from requests_html import HTMLSession
import src
from config import h1_dummy_endpoint


class Test:
    @pytest.fixture
    def mock_event(self):
        return {"foo": "bar"}

    def test_local_html_scrape(self, mock_event):
        session = HTMLSession()
        resp = session.get(h1_dummy_endpoint)
        print(resp)
        assert True

