import toml
import re


class SecurityWord(object):
    """
    Class for Security related words that are often misspelled
    """
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


