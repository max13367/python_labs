if __name__ == "__main__" and __package__ is None:
    __package__ = "src.lab03"

from ..lib.text import normalize, tokenize, count_freq, top_n

import sys
import io

def main():
    text = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8').read()
    print(f"Входной текст (raw): '{text}'")
    norm_text = normalize(text)
    tokens = tokenize(norm_text)
    freq = count_freq(tokens)
    top = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()
