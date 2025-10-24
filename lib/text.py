import re
from collections import Counter
from typing import Dict, List, Tuple

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = re.compile(r"[\t\r\n]+").sub(" ", text)
    text = re.compile(r"\s+").sub(" ", text).strip()
    return text

def tokenize(text: str) -> List[str]:
    return re.compile(r"[^\W_]+(?:-[^\W_]+)*", flags=re.UNICODE).findall(text)

def count_freq(tokens: List[str]) -> Dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    if n <= 0:
        return []
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

if __name__ == "__main__":
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize(" двойные пробелы ") == "двойные пробелы"

    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]

    print("все правильно")