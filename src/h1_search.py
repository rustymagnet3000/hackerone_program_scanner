import toml
import re
from conf.base_logger import logger


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


def get_all_spellings(words: dict):
    """
    :param words: original dict of all words and misspellings. Using Dict due to Toml Module
    :return:generator of bad spellings
    """
    for word in words.get('sec_words'):
        for bad_spellings in words.get('sec_words').get(word).get('patterns'):
            yield bad_spellings
    logger.info(f"Retrieved all incorrect spellings")


def search_h1_web_data(company_name, misspelled_words_lists, web_text):
    """
    :param web_text: scraped h1_program_notes
    :param misspelled_words_lists: For example: [['foxxx', 'foxx'],['miice']]
    :param company_name: name of H1 Company being analyzed
    :return:generator of results
    """
    for spellings in misspelled_words_lists:
        yield [(company_name, s) for s in spellings if re.match(s, web_text, flags=re.I | re.A)]
    logger.debug(f"Checked all spellings against {company_name}")
