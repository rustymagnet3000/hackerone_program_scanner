import pytest
# from conf.config import SecurityWord
import toml
from conf.base_logger import logger


def get_word_file(file_loc='../conf/words.toml') -> dict:
    """
    :param file_loc: location of toml file that contains all words
    :return: dict of all words found
    """
    words_dict = toml.load(file_loc)
    return words_dict


def bad_security_word_search(words: dict) -> list:
    """
    :param words: original dict of all words and misspellings
    :return:list_word_objs that better enable tracking
    """
    list_word_objs = []
    words = toml.load()
    for word in words.get('sec_words').keys():
        word_to_check = SecurityWord(word, words.get('sec_words').get(word).get('patterns'))
        list_word_objs.append(word_to_check)
    return list_word_objs


def bad_security_word_search(h1_program_notes, misspelled_word):
    """
        Search through the scraped h1_program_notes against a mispelled word
    :return:
    """

    return None


class SecurityWord(object):
    """
      Class for Security related words that are often misspelled
    """
    word_and_patterns: dict
    found_something: bool
    results: dict       # name of web program found and result

    def __init__(self, word: str, patterns: list):
        self.original_word = word.lower()
        self.incorrect_spellings = frozenset(patterns)
        self.results = {}


class TestH1SecSpellings:

    dummy_text = """ the quick brown
            fox jumped over the very large
            brown log ..."""

    def test_load_word_file(self):
        words = toml.load('../conf/words.toml')
        assert isinstance(words, dict)

    def test_bad_file_location(self):
        try:
            words = toml.load('../black/hole.toml')
            logger.warning("Unexpectedly loaded a file")
            assert False
        except FileNotFoundError:
            assert True

    def test_words_loaded_correctly(self):
        words = toml.load('../conf/words.toml')
        assert len(words.get('sec_words')) > 0

    def test_init_classes_from_file(self):
        """
        Get the word file. Init a Class with the values.
        :return:
        """
        words_list = []
        words = toml.load('../conf/words.toml')
        for word in words.get('sec_words').keys():
            word_to_check = SecurityWord(word, words.get('sec_words').get(word).get('patterns'))
            words_list.append(word_to_check)
        print(words_list)

    def test_search_text_bad_word(self):
        """
        For each locally listed Security Word get the patterns.
        Check them against a big string of data.
        :return:
        """
        words = toml.load('../conf/words.toml')
        patterns = words.get('sec_words').values()
        for pattern in patterns:
            logger.info(pattern)

    def test_basic_security_word(self):
        a = SecurityWord('malicious', ['Melicious'])
        assert isinstance(a, SecurityWord)

    def test_str_as_pattern_list(self):
        word = SecurityWord('malicious', 'Melicious')
        assert True

    def test_strs_as_pattern_list(self):
        word = SecurityWord('malicious', 'Melicious,Boo')
        assert True

    def test_init_with_multiple_bad_patterns(self):
        a = SecurityWord('malicious', ['Malicious', 'Malicoius', 'MalicOUs'])

        assert True