import bs4
import requests
import nlp_utils
import regex_utils



def combine_paragraphs(soup : bs4.BeautifulSoup) -> str:
    """Combines all paragraph elements of a soup object into a string"""
    combined_text = ""
    paragraphs = soup.find_all("p")
    for p in paragraphs:
        clean_paragraph = regex_utils.remove_references(p.text)
        combined_text += clean_paragraph
    return combined_text


def article_text(article_url : str) -> str|None:
    """Gets the article text from a given article"""
    try:
        response = requests.get(url = article_url)
        raw_html = response.text
        soup = bs4.BeautifulSoup(raw_html, "html.parser")  
        article_text = combine_paragraphs(soup)
        return article_text
    except Exception:
        return None


def summarize_article(article_url : str) -> str|None:
    article_text = article_text(article_url)
    if article_text is not None:
        article_summary = nlp_utils.summarize_text(article_text)
        return article_summary
    else:
        return None


# Testing
WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/Matthew_Dominick"
article_text = article_text(WIKIPEDIA_URL)
print(article_text)