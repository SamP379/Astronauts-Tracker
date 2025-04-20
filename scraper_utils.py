import bs4
import requests


def combine_paragraphs(soup : bs4.BeautifulSoup) -> str:
    """Returns all paragraph elements of a soup object combined into a string"""
    combined_text = ""
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        combined_text += p.text
    return combined_text


def article_text(article_url : str) -> str|None:
    """Returns the article text from a given article or None if not found"""
    try:
        response = requests.get(url = article_url)
        raw_html = response.text
        soup = bs4.BeautifulSoup(raw_html, "html.parser")  
        text = combine_paragraphs(soup)
        return text
    except Exception as error:
        raise error
        return None