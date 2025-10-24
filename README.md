# python_labs

## Лабораторная работа 1

### Задание 1

```
name = input()
age = int(input())
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```

![фото1](./images/lab01/01.png)


### Задание 2

```
a = float(input().replace(',', '.'))
b = float(input().replace(',', '.'))
sum_ = a + b
avg_ = sum_ / 2
print(f"sum={sum_:.2f}; avg={avg_:.2f}")
```

![фото2](./images/lab01/02.png)


### Задание 3

```
price = int(input())
discount = int(input())
vat = int(input())

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f"База после скидки: {base:.2f} $")
print(f"Ндс              : {vat_amount:.2f} $")
print(f"Итого к оплате   : {total:.2f} $")
```

![фото3](./images/lab01/03.png)



### Задание 4

```
m = int(input())

hours = m // 60
minutes = m % 60

print(f"{hours}:{minutes:02d}")
```

![фото4](./images/lab01/04.png)


### Задание 5

```
fio_input = input()
fio_new = ' '.join(fio_input.split())

words = fio_new.split()

initials = ''.join([word[0].upper() for word in words])

length = len(fio_new)

print(f"ФИО             : {fio_input}")
print(f"Инициалы        : {initials}.")
print(f"Длина (символов): {length}")
```

![фото5](./images/lab01/05.png)


### Задание 6

```
n = int(input())
ochn = 0
zaochn = 0
for i in range(n):
    name = input().split()
    if 'True' in name:
        ochn += 1
    else:
        zaochn += 1
print(ochn, zaochn)
```

![фото6](./images/lab01/06.png)


### Задание 7

```
str_ = str(input())

newstr_ = ''
index_first = -1
index_second = -1
index_last = -1

for i in str_:
    index_first += 1
    if i.isupper():
        break

for i in range(len(str_) - 1):
    if str_[i].isdigit():
        index_second = i + 1
        break

for i in str_:
    index_last += 1
    if i == '.':
        break
        

shag = index_second - index_first

for i in range(index_first, index_last + 1, shag):
    newstr_ += str_[i]
print(newstr_)
```

![фото7](./images/lab01/07.png)


## Лабораторная работа 2

### Задание 1

```
def min_max(a):
    if not a:
        return 'ValueError'

    max_ = -10 ** 10
    min_ = 10 ** 10
    for i in a:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i

    return (min_, max_)


def unique_sorted(b):
    return sorted(set(b))


def flatten(c):
    if not c:
        return []

    result = []

    for i in c:
        if not isinstance(i, (list, tuple)):
            return 'TypeError'
        result.extend(i)

    return result
```

![фото1 2](./images/lab02/01.png)


### Задание 2

```
def transpose(a):
    if not a:
        return []

    first_riad = len(a[0])
    for i in a:
        if len(i) != first_riad:
            return 'ValueError'

    result = []
    for stolb in range(len(a[0])):
        new_riad = []
        for riad in range(len(a)):
            new_riad.append(a[riad][stolb])
        result.append(new_riad)

    return result

def row_sums(b):
    if not b:
        return []

    first_riad = len(b[0])
    for i in b:
        if len(i) != first_riad:
            return 'ValueError'

    result = []
    for row in b:
        result.append(sum(row))
    return result

def col_sums(c):
    if not c:
        return []

    first_riad = len(c[0])
    for i in c:
        if len(i) != first_riad:
            return 'ValueError'

    result = []
    for stolb in range(len(c[0])):
        sum_ = 0
        for riad in range(len(c)):
            sum_ += c[riad][stolb]
        result.append(sum_)

    return result
```

![фото2 2](./images/lab02/02.png)


### Задание 3

```
def format_record(rec: tuple[str, str, float]) -> str:
    student, gruppa, gpa = rec
    
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")

    if not student or not student.strip():
        raise ValueError("ФИО студента не может быть пустым")

    if not gruppa or not gruppa.strip():
        raise ValueError("Номер группы не может быть пустым")


    student = student.strip().title()
    parts = [part for part in student.split() if part]


    if len(parts) < 1:
        raise ValueError("ФИО должно содержать хотя бы фамилию")

    student = student.title()
    parts = student.split()
    familiya = parts[0]
    new_fam = []
    if len(parts) > 1:
        new_fam.append(parts[1])
    if len(parts) > 2:
        new_fam.append(parts[2])

    initial = []
    for i in new_fam:
        initial.append(i[0] + '.')


    initials_str = ''.join(initial)
    fio = f'{familiya} {initials_str}, гр. {gruppa}, GPA {gpa:.2f}'
    return fio
```

![фото3 2](./images/lab02/03.png)

## Лабораторная работа 3

### Задание 1

```
import re
from collections import Counter
from typing import Dict, List, Tuple

_WORD_RE = re.compile(r"\w+(?:-\w+)*", flags=re.UNICODE)
_WS_NL_RE = re.compile(r"[\t\r\n]+")
_WS_RE = re.compile(r"\s+")


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    text = _WS_NL_RE.sub(" ", text)
    text = _WS_RE.sub(" ", text).strip()
    return text


def tokenize(text: str) -> List[str]:
    return _WORD_RE.findall(text)


def count_freq(tokens: List[str]) -> Dict[str, int]:
    return dict(Counter(tokens))


def top_n(freq: Dict[str, int], n: int = 5) -> List[Tuple[str, int]]:
    if n <= 0:
        return []
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
```

![фото1 3](./images/lab03/01.png)

### Задание 2

```
from __future__ import annotations

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n


def main() -> None:
    # Читаем весь stdin до EOF
    data = sys.stdin.read()

    norm = normalize(data)
    tokens = tokenize(norm)
    freq = count_freq(tokens)
    top = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, cnt in top:
        print(f"{word}:{cnt}")


if __name__ == "__main__":
    main()
```

![фото2 3](./images/lab03/02.png)

## Лабораторная работа 4

### Задание 1

```
import csv
from pathlib import Path
from typing import Iterable, Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: Iterable[Sequence], path: Union[str, Path],
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows_list = list(rows)

    if rows_list:
        first_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалась {first_len}")

    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
```

![фото1 4](./images/lab04/01.png)

### Задание 2

```
import sys
import argparse
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent.parent))

from lib.text import normalize, tokenize, top_n
from lab04.io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def print_formatted_table(freq: dict[str, int], title: str = "Статистика слов"):
    sorted_items = sorted_word_counts(freq)
    if not sorted_items:
        print("Нет данных для отображения")
        return

    max_word_len = max(len(word) for word, _ in sorted_items)
    max_count_len = max(len(str(count)) for _, count in sorted_items)

    print(f"\n{title}")
    print("=" * (max_word_len + max_count_len + 5))

    for word, count in sorted_items:
        print(f"{word:<{max_word_len}} | {count:>{max_count_len}}")

    print()


def generate_single_file_report(input_file: str, output_file: str, encoding: str = "utf-8") -> None:
    try:
        text = read_text(input_file, encoding)
        freq = frequencies_from_text(text)
        sorted_freq = sorted_word_counts(freq)

        write_csv(sorted_freq, output_file, header=("word", "count"))

        total_words = sum(freq.values())
        unique_words = len(freq)
        top_words = top_n(freq, 5)

        print(f"Файл: {input_file}")
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")

        print_formatted_table(freq, f"Топ-слов из {input_file}")

        print(f"Отчет сохранен: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка декодирования: {e}")
        print("Попробуйте указать правильную кодировку через --encoding")
        sys.exit(1)


def generate_multi_file_report(input_files: list, per_file_output: str,
                               total_output: str, encoding: str = "utf-8") -> None:
    all_freq = Counter()
    per_file_data = []
    processed_files = 0

    for file_path in sorted(input_files):
        try:
            text = read_text(file_path, encoding)
            freq = frequencies_from_text(text)
            all_freq.update(freq)

            for word, count in sorted_word_counts(freq):
                per_file_data.append((str(file_path), word, count))

            processed_files += 1
            print(f"✓ Обработан: {file_path} (слов: {sum(freq.values())}, уникальных: {len(freq)})")

        except FileNotFoundError:
            print(f"✗ Ошибка: Файл '{file_path}' не найден, пропускаем")
        except UnicodeDecodeError as e:
            print(f"✗ Ошибка декодирования в файле '{file_path}': {e}")

    if processed_files == 0:
        print("Не удалось обработать ни одного файла")
        sys.exit(1)

    write_csv(per_file_data, per_file_output, header=("file", "word", "count"))

    write_csv(sorted_word_counts(all_freq), total_output, header=("word", "count"))

    print(f"\nИтоговая статистика:")
    print(f"Обработано файлов: {processed_files}")
    print(f"Всего уникальных слов: {len(all_freq)}")
    print(f"Общее количество слов: {sum(all_freq.values())}")

    print_formatted_table(all_freq, "Сводная статистика по всем файлам")

    print(f"Отчет по файлам сохранен: {per_file_output}")
    print(f"Сводный отчет сохранен: {total_output}")


def main():
    parser = argparse.ArgumentParser(description='Анализ текстовых файлов и генерация отчетов')

    # Основные аргументы
    parser.add_argument('--in', dest='input_files', nargs='+',
                        help='Входные файлы для анализа')
    parser.add_argument('--out', dest='output_file',
                        default='data/lab04/report.csv',
                        help='Путь для сохранения отчета (для одного файла)')
    parser.add_argument('--encoding', default='utf-8',
                        help='Кодировка файлов (по умолчанию: utf-8)')

    # Аргументы для режима нескольких файлов
    parser.add_argument('--per-file', dest='per_file_output',
                        help='Путь для отчета по каждому файлу (режим нескольких файлов)')
    parser.add_argument('--total', dest='total_output',
                        help='Путь для сводного отчета (режим нескольких файлов)')

    args = parser.parse_args()

    if args.per_file_output or args.total_output:
        if not args.input_files:
            print("Ошибка: для режима нескольких файлов укажите --in с списком файлов")
            sys.exit(1)

        per_file_out = args.per_file_output or 'data/lab04/report_per_file.csv'
        total_out = args.total_output or 'data/lab04/report_total.csv'

        generate_multi_file_report(args.input_files, per_file_out, total_out, args.encoding)

    else:
        input_file = args.input_files[0] if args.input_files else 'data/lab04/input.txt'
        generate_single_file_report(input_file, args.output_file, args.encoding)


if __name__ == "__main__":
    main()
```

![фото2 4](./images/lab04/02.png)
![фото2 5](./images/lab04/03.png)