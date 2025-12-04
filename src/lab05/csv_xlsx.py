from pathlib import Path
import csv
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    p_csv = Path(csv_path)
    p_xlsx = Path(xlsx_path)
    # Проверки путей
    if p_csv.suffix.lower() != ".csv":
        raise ValueError("Ожидается файл с расширением .csv")
    if p_xlsx.suffix.lower() != ".xlsx":
        raise ValueError("Ожидается файл с расширением .xlsx")

    if not p_csv.exists():
        raise FileNotFoundError("Файл CSV не найден")

    # Чтение CSV
    with p_csv.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Проверка содержимого
    if not rows or all(not any(row) for row in rows):
        raise ValueError("Пустой CSV или неподдерживаемая структура")

    # Создание XLS
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Автоширина
    for col in ws.columns:
        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len + 2, 8)

    # Проверка директории назначения
    if not p_xlsx.parent.exists():
        raise FileNotFoundError(f"Директория для XLSX не найдена")

    # Сохранение
    wb.save(p_xlsx)


# ПРИМЕР
# Конвертация people.csv → people.xlsx
# csv_to_xlsx("data2/samples/people.csv", "data2/out/people1.xlsx")

# csv_input = Path("data2/samples/cities.csv")
# xlsx_output = Path("data2/out/cities.xlsx")

## Создаём папку out, если её нет
# xlsx_output.parent.mkdir(parents=True, exist_ok=True)
# csv_input.parent.mkdir(parents=True, exist_ok=True)

## Записываем пример в CSV
# example_rows = [
#    ["city", "country", "language"],
#    ["Moscow", "Russia", "Russian"],
#    ["Tokyo", "Japan", "Japanese"],
#    ["Paris", "France", "French"],
# ]
# with csv_input.open("w", newline="", encoding="utf-8") as f:
#    writer = csv.writer(f)
#    writer.writerows(example_rows)

# Конвертация CSV → XLSX
# csv_to_xlsx(csv_input, xlsx_output)

# Ошибки
# csv_to_xlsx("data2/samples/people_empty.csv", "data2/samples/people.xlsx")
# csv_to_xlsx("data2/samples/people_dsadasdw.csv", "data/samples/people.xlsx")
# csv_to_xlsx("data2/samples/xcaca.csv", "data/samples/people.json")

# Пример работы
## Конвертация people.csv → people.xlsx
# csv_to_xlsx("data2/samples/people.csv", "data2/out/people.xlsx")

# csv_input = Path("data2/samples/cities.csv")
# xlsx_output = Path("data2/out/cities.xlsx")

## Создаём папку out, если её нет
# xlsx_output.parent.mkdir(parents=True, exist_ok=True)
# csv_input.parent.mkdir(parents=True, exist_ok=True)

## Записываем любой пример в CSV
# example_rows = [
#    ["city", "country", "language"],
#    ["Moscow", "Russia", "Russian"],
#    ["Tokyo", "Japan", "Japanese"],
#    ["Paris", "France", "French"],
# ]
# with csv_input.open("w", newline="", encoding="utf-8") as f:
#    writer = csv.writer(f)
#    writer.writerows(example_rows)

# Конвертация CSV → XLSX
# csv_to_xlsx(csv_input, xlsx_output)
