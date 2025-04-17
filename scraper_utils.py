import bs4
import requests

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