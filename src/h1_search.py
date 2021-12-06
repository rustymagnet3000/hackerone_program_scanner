import toml
import re
from itertools import chain


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
    :return:small generator
    """
    for word in words.get('sec_words'):
        for bad_spellings in words.get('sec_words').get(word).get('patterns'):
            yield bad_spellings


def get_all_spellings_to_check(words: list):
    """
    :param words: list of SecurityWords
    :return:small generator
    """
    for word in words:
        yield [bad_spelling for bad_spelling in word.incorrect_spellings]


# for word in words:
   #     yield (bad_spelling for bad_spelling in word.incorrect_spellings)


def search_h1_web_data(misspelled_words: list, web_text):
    return [bad_spelling for bad_spelling in misspelled_words if re.search(bad_spelling, web_text)]


def search_h1_program_notes_for_misspellings(company: str, h1_program_notes: str, sec_words: SecurityWord):
    """
    :param company: name of H1 Company being analyzed
    :param h1_program_notes: scraped h1_program_notes
    :param sec_words: objects to check
    :return:small generator
    """

    list_of_bad_spellings_sets = chain([word.incorrect_spellings for word in sec_words])
#    results = [{'id':company, 'found': s}, search_h1_web_data(s, h1_program_notes) for s in list_of_bad_spellings_sets]
#   return results


