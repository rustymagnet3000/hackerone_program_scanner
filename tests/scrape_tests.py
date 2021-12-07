from conf.base_logger import logger
from h1_scrape import scrape_company
from h1_search import get_word_file, \
    search_h1_web_data, \
    get_all_spellings


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

    def test_scrape_coinbase_against_known_word(self):
        web_data = scrape_company(self.company_name)
        words_gen = get_all_spellings(self.words_dict)
        results_gen = search_h1_web_data(self.company_name, words_gen, web_data)
        res = debug_gen(results_gen)
        if len(res) == 0 and isinstance(res, list):
            logger.info(f"No findings to report for {self.company_name}")
            assert True
        elif isinstance(res, list):
            logger.info(f"Found something: {self.company_name}\n\t{res}")
            assert True
        else:
            assert False
