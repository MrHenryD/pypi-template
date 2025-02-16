import re


def remove_digits(text: str) -> str:
    return "".join([char for char in text if not char.isdigit()])


def remove_special_characters(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9 ]+", "", text)
