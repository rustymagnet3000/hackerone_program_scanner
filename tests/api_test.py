import pytest

from conf.config import api_get_programs_endpoint
from h1_creds import check_h1_credentials_exist, H1creds
from h1_info import get_h1_programs, send_request, clean_companies_file


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
        resp = get_h1_programs(self.creds.username, self.creds.access_token, next_url=api_get_programs_endpoint)
        assert isinstance(resp, list) and len(resp) > 0

    def test_write_results_to_file_limit_results(self):
        result = get_h1_programs(self.creds.username,
                                 self.creds.access_token,
                                 next_url=api_get_programs_endpoint,
                                 limit_results=True)
        assert result is True

    def test_remove_companies_file(self):
        clean_companies_file()
        assert True

