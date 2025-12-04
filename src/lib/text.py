import re


def normalize(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be string")

    # нижний регистр
    text = text.lower()

    # замена ё → е (по-русски)
    text = text.replace("ё", "е")

    # переводы строк/табов → пробелы
    text = re.sub(r"[\n\r\t]+", " ", text)

    # один пробел между словами
    text = re.sub(r"\s+", " ", text).strip()

    return text


import re

import re


def tokenize(text: str) -> list[str]:

    tokens = re.findall(r"[A-Za-zА-Яа-я0-9_]+(?:-[A-Za-zА-Яа-я0-9_]+)*", text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    fdict = {}
    for token in tokens:
        if token in fdict:
            fdict[token] += 1
        else:
            fdict[token] = 1
    return fdict


def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
