import re
from collections import Counter
from typing import Dict, List, Tuple

# Улучшенные регулярные выражения для Unicode
_WORD_RE = re.compile(r"[^\W_]+(?:-[^\W_]+)*", flags=re.UNICODE)
_WS_NL_RE = re.compile(r"[\t\r\n]+")
_WS_RE = re.compile(r"\s+")

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """
    Нормализация текста:
    - при yo2e=True заменяет ё/Ё -> е/Е
    - при casefold=True приводит к casefold()
    - заменяет \t, \r, \n на пробел
    - схлопывает все последовательности пробелов и обрезает края
    """
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = _WS_NL_RE.sub(" ", text)
    text = _WS_RE.sub(" ", text).strip()
    return text

def tokenize(text: str) -> List[str]:
    """
    Токенизация:
    - слова это шаблон [^\W_]+(?:-[^\W_]+)*
    - работает с Unicode буквами (кириллица, латиница)
    - дефис разрешен только внутри слова
    - числа тоже считаются словами
    """
    return _WORD_RE.findall(text)

def count_freq(tokens: List[str]) -> Dict[str, int]:
    """Подсчитывает частоты слов из списка токенов."""
    return dict(Counter(tokens))

def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    """
    Возвращает топ-N пар (слово, частота), сортировка по ключу (-частота, слово).
    При n <= 0 возвращает пустой список.
    """
    if n <= 0:
        return []
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]

if __name__ == "__main__":
    # Мини-тесты
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

    print("OK")