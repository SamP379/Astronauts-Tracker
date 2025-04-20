import re


REFERENCES_PATTERN = r"\[\d*\]"


def remove_references(text : str) -> str:
    new_text = re.sub(REFERENCES_PATTERN, "", text)
    return new_text