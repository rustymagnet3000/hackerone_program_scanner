import pytest
from h1_creds import check_h1_credentials_exist, H1creds
from h1_info import get_h1_programs, send_request, write_results_to_file
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

    def test_h1_list_builder(self):
        resp = get_h1_programs(self.creds.username, self.creds.access_token)
        assert isinstance(resp, list) and len(resp) > 0

    def test_write_results_to_file(self):
        res_list = get_h1_programs(self.creds.username, self.creds.access_token)
        outcome = write_results_to_file(res_list)
        assert outcome is True