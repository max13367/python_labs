from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Считывает текст из .txt файла"""
    p = Path(path)
    if p.suffix.lower() != ".txt":
        raise ValueError("Неправильный формат — требуется файл с расширением txt.")
    try:
        return p.read_text(encoding=encoding)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл не найден: {p}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Ошибка декодирования. Попробуйте другую кодировку.")


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    if p.suffix.lower() != ".csv":
        raise ValueError("Неправильный формат — требуется файл с расширением .csv")

    rows = list(rows)
    if rows:
        length = len(rows[0])
        for r in rows:
            if len(r) != length:
                raise ValueError("Все строки должны иметь одинаковую длину")

    if header is not None and rows:
        if len(header) != len(rows[0]):
            raise ValueError("Длина заголовка не совпадает с длиной строк данных")

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

# Тестовые задания

if __name__ == "__main__":
    # Задание A
    Path("data").mkdir(exist_ok=True)
    (Path("data") / "input.txt").write_text("Привет, мир! Привет!!!", encoding="utf-8")
    print("Файл data/input.txt создан")

    # Задание B
    def print_csv(path):
        p = Path(path)
        with p.open('r', encoding='utf-8') as f:
            for line in f:
                print(line.strip())

    write_csv([], "data/empty.csv", header=("a", "b"))
    print_csv("data/empty.csv")

    write_csv([("word", "count"), ("test", 3)], "data/check.csv")
    print_csv("data/check.csv")

    txt = read_text(Path("data") / "input.txt")
    print("Содержимое input.txt:", txt)
    csv_path = Path("data") / "report.csv"
    write_csv([("word", "count"), ("привет", 2)], csv_path, header=("word", "count"))
    print("Создан CSV:", csv_path)

    try:
        (Path("data") / "1251input.txt").write_text("Привет из cp1251", encoding="cp1251")
        str_cp1251 = read_text("data/1251input.txt", encoding='cp1251')
        print("Прочитано из cp1251:", str_cp1251)
    except Exception as e:
        print("Ошибка при чтении cp1251 файла:", e)