import pytest
from h1_creds import check_h1_credentials_exist, H1creds
from h1_info import get_h1_programs, send_request
from requests import Response


class TestAPIRequests:

    creds = check_h1_credentials_exist()

    @pytest.fixture
    def h1_api_request(self):
        return None

    def test_h1_credentials_exist(self):
        assert isinstance(self.creds, H1creds) and self.creds is not None

    def test_h1_send_request(self):
        resp = send_request(self.creds.username, self.creds.access_token)
        assert resp.ok
