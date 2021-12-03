import toml
import re
from itertools import chain


class SecurityWord(object):
    """
    Class for Security related words that are often misspelled
    """
    def __init__(self, word: str, patterns: list):
        self.original_word = word.lower()
        self.incorrect_spellings = patterns


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


def search_h1_web_data(misspelled_words: list, web_text) -> list:
    results = [bad_spelling for bad_spelling in misspelled_words if re.search(bad_spelling, web_text)]
    return results


def search_h1_program_notes_for_misspellings(company: str, h1_program_notes: str, sec_words: SecurityWord) -> dict:
    """
    :param company: name of H1 Company being analyzed
    :param h1_program_notes: scraped h1_program_notes
    :param sec_words: objects to check
    :return:
    """

    list_of_bad_spellings_sets = chain([word.incorrect_spellings for word in sec_words])
    results = [search_h1_web_data(s, h1_program_notes) for s in list_of_bad_spellings_sets]
    return results


