import pytest
from conf.base_logger import logger


class TestH1SecSpellings:
    company_name = 'foobar'
    dummy_text = """ the quick brown
            fox foxx foxxx jumped over the very large
            brown log ..."""

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
        Get the word file. Init a Class with the values.
        :return:
        """
        words_dict = get_word_file()
        words_list = get_word_objects_to_search(words_dict)
        assert len(words_list) > 0 and isinstance(words_list, list)

    def test__foxx_found_in_search(self):
        words_dict = get_word_file()
        word_objs = get_word_objects_to_search(words_dict)
        results = search_h1_program_notes_for_misspellings(self.company_name, self.dummy_text, word_objs)
        assert len(results) > 0 and isinstance(results, list)
