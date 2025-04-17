import bs4
import requests


def combine_paragraphs(soup : bs4.BeautifulSoup) -> str:
    """Combines all parapgraph elements of a soup object into a string"""
    paragraphs_text = ""
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        paragraphs_text += p.text
    return paragraphs_text


def get_article_text(article_url : str) -> str|None:
    """Gets the article text (paragraph elements) from a given article"""
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