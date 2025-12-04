import argparse
from src.lib.text import tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(
        description="Инструмент для работы с текстовыми файлами"
    )
    cmds = parser.add_subparsers(dest="mode")

    # cat
    cmd_cat = cmds.add_parser("cat", help="Показать файл целиком")
    cmd_cat.add_argument("--file", required=True, help="Файл для чтения")
    cmd_cat.add_argument(
        "-n", "--nums", action="store_true", help="Выводить номера строк"
    )

    # stats
    cmd_stats = cmds.add_parser("stats", help="Подсчёт встречаемости слов")
    cmd_stats.add_argument("--file", required=True, help="Исходный текст")
    cmd_stats.add_argument("--k", type=int, default=5, help="Сколько слов вывести")

    opt = parser.parse_args()

    if opt.mode == "cat":
        with open(opt.file, encoding="utf-8") as fh:
            for idx, line in enumerate(fh, 1):
                line = line.rstrip()
                print(f"{idx}: {line}" if opt.nums else line)

    elif opt.mode == "stats":
        with open(opt.file, encoding="utf-8") as fh:
            data = fh.read()
        words = tokenize(data)
        freq = count_freq(words)
        for w, c in top_n(freq, opt.k):
            print(f"{w}: {c}")


if __name__ == "__main__":
    main()
