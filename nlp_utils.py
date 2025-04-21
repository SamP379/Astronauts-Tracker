import re
import nltk
nltk.download('punkt_tab')


STOPWORDS = nltk.corpus.stopwords.words('english')

 
def preprocess_text(text : str) -> str:
    """Remove Wikipedia references, newlines, and extra whitespace from the text."""
    preprocessed_text = re.sub(r"\[\d*\]", "", text)
    preprocessed_text = re.sub(r"\n", "", preprocessed_text)
    preprocessed_text = re.sub(r"\s+", " ", preprocessed_text)
    return preprocessed_text


def format_text(text : str) -> str:
    "Removes non a-z characters and extra whitespace from the text"
    formatted_text = re.sub(r"[^a-zA-Z]", " ", text)
    formatted_text = re.sub(r"\s+", " ", formatted_text)
    return formatted_text


def calculate_word_frequencies(words_list : list) -> dict:
    word_frequencies = {}
    for word in words_list:
        if word not in STOPWORDS:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
    return word_frequencies


def normalize_word_frequencies(word_frequencies : dict) -> dict:
    maximum_frequncy = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / maximum_frequncy
    return word_frequencies


def summarize_text(text : str) -> str:

    clean_text = preprocess_text(article_text)
    formatted_text = format_text(clean_text)

    sentence_list = nltk.sent_tokenize(clean_text)

    words_list = nltk.word_tokenize(formatted_text)
    word_frequencies = calculate_word_frequencies(words_list)
    word_frequencies = normalize_word_frequencies(word_frequencies)






# --------------------- Testing code -------------------------- # 
import scraper_utils

url = "https://en.wikipedia.org/wiki/My_Darling_Clementine"
article_text = scraper_utils.article_text(url)
if article_text is None:
    print("No article found")
    exit()
# --------------------- Testing code -------------------------- #