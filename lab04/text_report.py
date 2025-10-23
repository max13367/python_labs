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