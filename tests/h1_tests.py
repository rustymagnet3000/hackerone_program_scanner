import pytest
from conf.base_logger import logger
from h1_search import get_word_file, \
    search_h1_program_notes_for_misspellings, \
    search_h1_web_data, SecurityWord, \
    get_all_spellings_to_check, \
    get_all_spellings


class TestH1SecSpellings:
    words_dict = get_word_file()
    company_name = 'foobar'
    dummy_text = """ the quick brown
            fox foxx foxxx jumped over the very large
            brown log ..."""
    bad_foxes = ['foxxx', 'foxx', 'foxxxx', 'fixx']

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
        words = get_word_file()
        assert len(words.get('sec_words')) > 0

    def test_init_classes_from_file(self):
        """
        Get the word file as a generator.  Unwrap generator as the file is small.
        """
        words_dict = get_word_file()
        words_gen = get_all_spellings(words_dict)
        assert len(list(words_gen)) > 0

    def test_init_single_class(self):
        fox_word = [SecurityWord('fox', self.bad_foxes)]
        assert len(fox_word) == 1

    def test_get_all_spellings_to_check(self):
        fox_word = [SecurityWord('fox', self.bad_foxes)]
        words_to_search = get_all_spellings_to_check(fox_word)
        bad_spellings = list(words_to_search)
        assert len(list(bad_spellings)) > 0

    def test_conversion_to_check(self):
        fox_word = [SecurityWord('fox', self.bad_foxes)]
        words_to_search = get_all_spellings_to_check(fox_word)
        bad_spellings = list(words_to_search)
        assert len(list(bad_spellings)) > 0


    def test_get_all_spellings_to_check_more_objects(self):
        fox_word = [
                        SecurityWord('fox', self.bad_foxes),
                        SecurityWord('mouse', self.bad_foxes)
        ]
        words_to_search = get_all_spellings_to_check(fox_word)
        bad_spellings = list(words_to_search)
        assert len(list(bad_spellings)) > 0

    def test_foxx_found_in_search(self):
        fox_word = [SecurityWord('fox', self.bad_foxes)]
        words_to_search = get_words_to_search()
        results = search_h1_program_notes_for_misspellings(self.company_name, self.dummy_text, fox_word)
        assert len(results) > 0 and isinstance(results, list)

    def test_new_search_streamlined(self):
        word_objs = get_words_to_search(self.words_dict)
        results = search_h1_program_notes_for_misspellings(self.company_name, self.dummy_text, word_objs)
        assert True

    def test_new_search_iterator(self):
        misspelled_foxes = ['foxxx', 'foxx', 'foxxxx', 'fixx']
        result = search_h1_web_data(misspelled_foxes, self.dummy_text)
        assert True
