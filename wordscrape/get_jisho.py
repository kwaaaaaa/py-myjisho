import headless
from bs4 import BeautifulSoup


def jisho_search(keyword):
    """
    Returns: definitions for word looked up
    """
    home_url = "http://jisho.org/"
    definitions = []

    # start browser session
    with headless.MechSession() as session:

        # open homepage and enter word
        session.open(home_url)
        session.select_form(id="search")
        session["keyword"] = keyword
        response = session.submit()
        soup = BeautifulSoup(response.read(), "html5lib")

        main_classes = soup.find_all('div', {'class': "concept_light clearfix"})
        for mc in main_classes:
            try:
                word = mc.find('span', {'class': 'text'}).text
                meaning = mc.find('span', {'class': 'meaning-meaning'}).text
                try:
                    pronounce = mc.find('span', {'class': 'furigana'}).text
                except:
                    pronounce = ''
                definitions.append({
                    'word': word.strip(),
                    'meaning': meaning.strip(),
                    'pronounce': pronounce,
                })
            except:
                pass

        return definitions
