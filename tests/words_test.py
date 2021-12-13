from conf.base_logger import logger
from h1_search import get_word_file, \
    SecurityWord, \
    search_h1_web_data, \
    get_all_spellings


def print_gen(results_gen):
    return [r for r in results_gen if len(r) > 0]


class TestH1SecSpellings:
    words_dict = get_word_file()
    company_name = 'foobar'
    dummy_text = """ the quick brown
            fox foxx foxxx jumped over the very large
            brown log ...to chase miice"""
    bad_foxes = ['foxxx', 'foxx', 'foxxxx', 'fixx', 'foox', 'ffox']
    bad_mice = ['miice', 'mic']

    def test_load_word_file(self):
        words = get_word_file()
        assert isinstance(words, dict)

    def test_bad_file_location(self):
        try:
            words = get_word_file('black/hole.toml')
            logger.warning("Unexpectedly loaded a file")
            assert False
        except FileNotFoundError:
            assert True
        else:
            assert False

    def test_words_loaded_correctly(self):
        assert len(self.words_dict.get('sec_words')) > 0

    def test_init_single_class(self):
        fox_word = [SecurityWord('fox', self.bad_foxes)]
        assert len(fox_word) == 1

    # Print all words listed in toml file
    def test_get_all_bad_spellings(self):
        from pprint import pprint
        words_gen = get_all_spellings(self.words_dict)
        pprint(print_gen(words_gen))
        assert True

    def test_get_fox_misspellings_single(self):
        fox_dict = {'sec_words': {'fox': {'patterns': [self.bad_foxes]}}}
        words_to_search = get_all_spellings(fox_dict)
        bad_foxes = list(words_to_search)
        assert len(list(bad_foxes)) > 0

    def test_get_animals_misspellings_single(self):
        fox_dict = {
                        'sec_words':
                        {
                            'fox': {'patterns': [self.bad_foxes]}
                        }
                   }
        words_to_search = get_all_spellings(fox_dict)
        bad_animals = list(words_to_search)
        assert len(list(bad_animals)) > 0

    def test_bad_foxes_found_in_search(self):
        fox_dict = {'sec_words': {'fox': {'patterns': [self.bad_foxes]}}}
        words_to_search = get_all_spellings(fox_dict)
        results_gen = search_h1_web_data(self.company_name, words_to_search, self.dummy_text)
        results = list(results_gen)
        assert len(results) > 0 and isinstance(results, list)

    def test_bad_animals_found_in_search(self):
        fox_dict = {
                        'sec_words':
                        {
                            'fox': {'patterns': [self.bad_foxes]},
                            'mice': {'patterns': [self.bad_mice]}
                        }
                   }
        words_to_search = get_all_spellings(fox_dict)
        results_gen = search_h1_web_data(self.company_name, words_to_search, self.dummy_text)
        results = list(results_gen)
        if len(results) == 0 and isinstance(results, list):
            logger.info(f"No findings to report for {self.company_name}")
            assert True