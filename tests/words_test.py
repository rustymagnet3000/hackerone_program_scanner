from conf.base_logger import logger
from h1_search import get_word_file, \
    SecurityWord, \
    search_h1_web_data, \
    get_all_spellings


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
    def test_get_count_bad_spellings(self):
        from pprint import pprint
        words_gen = get_all_spellings(self.words_dict)
        logger.info(f"{len(list(words_gen))}")
        assert True

    # Print all words listed in toml file
    def test_get_all_bad_spellings(self):
        from pprint import pprint
        words_list = get_all_spellings(self.words_dict)
        pprint(words_list)
        assert True

    def test_check_for_duplicates(self):
        import collections
        words_gen = get_all_spellings(self.words_dict)
        duplicates = ([item for item, count in collections.Counter(words_gen).items() if count > 1])
        if len(duplicates) > 0:
            logger.warning(f"Found duplicates values: {duplicates}")
            assert False

    def test_get_fox_misspellings_single(self):
        fox_dict = {'sec_words': {'fox': {'patterns': [self.bad_foxes]}}}
        words_to_search = get_all_spellings(fox_dict)
        assert len(words_to_search) > 0

    def test_get_animals_misspellings_single(self):
        fox_dict = {
                        'sec_words':
                        {
                            'fox': {'patterns': [self.bad_foxes]}
                        }
                   }
        words_to_search = get_all_spellings(fox_dict)
        assert len(words_to_search) > 0

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
