import re


REFERENCES_PATTERN = r"\[\d*\]"
NON_ALPHABET_PATTERN = r"[^a-zA-Z]"
SPACES_PATTERN = r"\s+"


def remove_references(text : str) -> str:
    new_text = re.sub(REFERENCES_PATTERN, "", text)
    return new_text


def format_text(text : str) -> str:
    formatted_text = re.sub(NON_ALPHABET_PATTERN, " ", text)
    formatted_text = re.sub(SPACES_PATTERN, ' ', formatted_text)
    return formatted_text