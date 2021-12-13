from conf.base_logger import logger
from h1_open_company_file import filter_company_file, open_file_of_companies
from h1_scrape import scrape_company
from h1_search import get_word_file, \
    search_h1_web_data, \
    get_all_spellings
from main import prime_time_scrape


def debug_gen(results_gen):
    return [r for r in results_gen if len(r) > 0]


class TestH1ScrapeFlow:
    words_dict = get_word_file()
    company_name = 'coinbase'
    fox_dict = {
        'sec_words':
            {
                'assets': {'patterns': ['assets']}
            }
    }

    def test_expect_no_findings_in_real_h1_profile(self):
        fox_dict = {
            'sec_words':
                {
                    'fox': {'patterns': ['foxes']}
                }
        }
        words_to_search = get_all_spellings(fox_dict)
        web_data = scrape_company(self.company_name)
        results_gen = search_h1_web_data(self.company_name, words_to_search, web_data)
        res = debug_gen(results_gen)
        assert len(res) == 0 and isinstance(res, list)

    # test I get results by reading file
    def test_open_file_of_companies(self):
        companies_list = open_file_of_companies()
        assert isinstance(companies_list, list)

    def test_read_and_print_all_company_names_from_local_file(self):
        targeted_h1_companies = filter_company_file()
        assert len(targeted_h1_companies) > 0
        for comp in targeted_h1_companies:
            logger.debug(f"{comp.name.ljust(25, ' ')}{comp.id.rjust(10, ' ')},")

    # The H1 sometimes return Company Names like "Yahoo!" or "Cloudflare Vulnerability Disclosure"
    # Even when regex applies, you can encounter HTTP404s
    def test_scrape_bad_company_name(self):
        import urllib
        try:
            scrape_company("cloudflarevulnerabilitydisclosure")
            assert False
        except urllib.error.HTTPError:
            assert True
        finally:
            pass

    def test_scrape_coinbase_against_known_word(self):
        web_data = scrape_company(self.company_name)
        words_gen = get_all_spellings(self.words_dict)
        results_gen = search_h1_web_data(self.company_name, words_gen, web_data)
        res = debug_gen(results_gen)
        if len(res) == 0 and isinstance(res, list):
            logger.info(f"No findings: {self.company_name}")
            assert True
        elif isinstance(res, list):
            logger.info(f"{self.company_name} found:\n\t{res}")
            assert True
        else:
            assert False

    def test_check_25_firms(self):
        words_gen = get_all_spellings(get_word_file())
        for c in filter_company_file():
            prime_time_scrape(c.name, words_gen)
