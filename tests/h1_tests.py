import pytest
# from conf.config import SecurityWord
import toml
from conf.base_logger import logger
import re


class SecurityWord(object):
    """
    Class for Security related words that are often misspelled
    """
    word_and_patterns: dict
    found_something: bool

    def __init__(self, word: str, patterns: list):
        self.original_word = word.lower()
        self.incorrect_spellings = frozenset(patterns)


def get_word_file(file_loc='../conf/words.toml') -> dict:
    """
    :param file_loc: location of toml file that contains all words
    :return: dict of all words found
    """
    words_dict = toml.load(file_loc)
    return words_dict


def get_word_objects_to_search(words: dict) -> list:
    """
    :param words: original dict of all words and misspellings
    :return:list_word_objs that better enable tracking
    """
    list_word_objs = []
    for word in words.get('sec_words').keys():
        word_to_check = SecurityWord(word, words.get('sec_words').get(word).get('patterns'))
        list_word_objs.append(word_to_check)
    return list_word_objs


def search_h1_program_notes_for_misspellings(company: str, h1_program_notes: str, sec_words: SecurityWord) -> dict:
    """
    :param company: name of H1 Company being analyzed
    :param h1_program_notes: scraped h1_program_notes
    :param sec_words: objects to check
    :return:
    """
    results = []
    for word in sec_words:
        for misspelling in word.incorrect_spellings:
            if re.search(misspelling, h1_program_notes):
                results.append([company, misspelling])
    return results


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
