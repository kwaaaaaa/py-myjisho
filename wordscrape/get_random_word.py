import headless
from bs4 import BeautifulSoup
import logging


"""
I thought to get a random word but it's better for user to enter word
"""


def random_english_word():
    """
    Returns: random word with defintion
    """
    home_url = "https://randomword.com/"

    # start browser session
    with headless.MechSession() as session:

        # open homepage to get a random word
        response = session.open(home_url)

        # read random word
        soup = BeautifulSoup(response.read(), "html5lib")
        word = soup.find('div', {'id': "random_word"}).text
        meaning = soup.find('div', {'id': "random_word_definition"}).text
        logging.info("found new word: {0} - {1}".format(word, meaning))
        print {
            'word': word,
            'meaning': meaning,
        }
        return {
            'word': word,
            'meaning': meaning,
        }
