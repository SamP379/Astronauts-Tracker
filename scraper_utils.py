import bs4
import requests
import regex_utils


def combine_paragraphs(soup : bs4.BeautifulSoup) -> str:
    """Combines all paragraph elements of a soup object into a string"""
    combined_text = ""
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        clean_paragraph = regex_utils.remove_references(p.text)
        combined_text += clean_paragraph
    return combined_text


def get_article_text(article_url : str) -> str|None:
    """Gets the article text from a given article"""
    try:
        response = requests.get(url = article_url)
        raw_html = response.text
        soup = bs4.BeautifulSoup(raw_html, "html.parser")  
        article_text = combine_paragraphs(soup)
        return article_text
    except Exception:
        return None


# Testing
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Matthew_Dominick"
article_text = get_article_text(WIKIPEDIA_URL)
print(article_text)