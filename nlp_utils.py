import re
import nltk
nltk.download('punkt_tab')

 
def preprocess_text(text : str) -> str:
    """Remove references, newlines, and extra whitespace from the text."""
    preprocessed_text = re.sub(r"\[\d*\]", "", text)
    preprocessed_text = re.sub(r"\n", "", preprocessed_text)
    preprocessed_text = re.sub(r"\s+", " ", preprocessed_text)
    return preprocessed_text


def format_text(text : str) -> str:
    "Removes non a-z characters and extra whitespace from the text"
    formatted_text = re.sub(r"[^a-zA-Z]", " ", text)
    formatted_text = re.sub(r"\s+", " ", formatted_text)
    return formatted_text




import scraper_utils

url = "https://en.wikipedia.org/wiki/My_Darling_Clementine"
article_text = scraper_utils.article_text(url)
if article_text is None:
    print("No article found")
    exit()


article_text = preprocess_text(article_text)
formatted_text = format_text(article_text)

stopwords = nltk.corpus.stopwords.words('english')
sentence_list = nltk.sent_tokenize(article_text)

word_frequencies = {}
words_list = nltk.word_tokenize(article_text)

for word in words_list:
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1