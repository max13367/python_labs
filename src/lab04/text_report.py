from pathlib import Path
from collections import Counter
from src.lib.text import normalize, tokenize, top_n
from src.lab04.io_txt_csv import read_text, write_csv


try:
    text = read_text(Path("data/input.txt"))
except FileNotFoundError:
    print(f"Файл не найден: {Path("data/input.txt")}")
    raise
except UnicodeDecodeError:
    print(f"Ошибка кодировки при чтении файла: {Path("data/input.txt")}")
    raise


def frequencies_from_text(text: str) -> dict[str, int]:
    from src.lib.text import normalize, tokenize, top_n  # из ЛР3

    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


text = sorted_word_counts(frequencies_from_text(read_text("data/input.txt")))
write_csv(text, "data/report.csv", header=("word", "count"))

tekst = read_text("data/input.txt")
tokens = tokenize(normalize(tekst))
count = Counter(tokens)
sorted_freq = sorted_word_counts(count)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(count)}")
print(f"Топ-5:")
for word, col in sorted_freq[:5]:
    print(f"{word}:{col}")
