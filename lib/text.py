
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = re.sub(r'\s+', ' ', text).strip()
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'e')
    return text

import re

def tokenize(text: str) -> list[str]:
    shablon = r'\w+(?:-\w+)*'
    tockens = (re.findall(shablon, normalize(text)))
    return tockens

testcase1 = ["a", "b", "a", "c", "b", "a"]
testcase2 = ["bb", "aa", "bb", "aa", "cc"]


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
