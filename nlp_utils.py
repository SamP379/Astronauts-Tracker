import re
import nltk
nltk.download('punkt_tab')

 
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



# --------------------- Testing code -------------------------- # 
import scraper_utils

url = "https://en.wikipedia.org/wiki/My_Darling_Clementine"
article_text = scraper_utils.article_text(url)
if article_text is None:
    print("No article found")
    exit()
# --------------------- Testing code -------------------------- # 


clean_text = preprocess_text(article_text)
formatted_text = format_text(clean_text)

stopwords = nltk.corpus.stopwords.words('english')

# Split text into a list of sentences and words
sentence_list = nltk.sent_tokenize(clean_text)
words_list = nltk.word_tokenize(formatted_text)

# Find the frequency of occurence of each word
word_frequencies = {}
for word in words_list:
    if word not in stopwords:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1


# Normalize frequencies 
maximum_frequncy = max(word_frequencies.values())
for word in word_frequencies:
    word_frequencies[word] = word_frequencies[word] / maximum_frequncy

print(word_frequencies)