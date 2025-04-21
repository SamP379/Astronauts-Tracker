import re
import nltk
import heapq
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


def calculate_sentence_scores(sentence_list : list, word_frequencies : dict) -> dict:
    sentence_scores = {}
    for sentence in sentence_list:
        if len(sentence.split(" ")) < 35:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequencies[word]
                    else:
                        sentence_scores[sentence] += word_frequencies[word]
    return sentence_scores


def summarize_text(text : str) -> str:
    clean_text = preprocess_text(text)
    formatted_text = format_text(clean_text)
    sentence_list = nltk.sent_tokenize(clean_text)
    words_list = nltk.word_tokenize(formatted_text)
    word_frequencies = calculate_word_frequencies(words_list)
    word_frequencies = normalize_word_frequencies(word_frequencies)
    sentence_scores = calculate_sentence_scores(sentence_list, word_frequencies)
    threshhold_score = max(sentence_scores.values()) * 0.60
    summary = ""
    for sentence in sentence_scores:
        if sentence_scores[sentence] > threshhold_score:
            summary += sentence + " "
    return summary