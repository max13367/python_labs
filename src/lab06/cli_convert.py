import argparse
import os
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертация форматов данных")
    commands = parser.add_subparsers(dest="action", required=True)

    # JSON → CSV
    c_json = commands.add_parser("json2csv", help="Преобразовать JSON в CSV")
    c_json.add_argument("--in", dest="src", required=True, help="Входной JSON файл")
    c_json.add_argument("--out", dest="dst", required=True, help="Куда сохранить CSV")

    # CSV → JSON
    c_csv = commands.add_parser("csv2json", help="Преобразовать CSV в JSON")
    c_csv.add_argument("--in", dest="src", required=True, help="Входной CSV файл")
    c_csv.add_argument("--out", dest="dst", required=True, help="Куда сохранить JSON")

    # CSV → XLSX
    c_xlsx = commands.add_parser("csv2xlsx", help="Преобразовать CSV в XLSX")
    c_xlsx.add_argument("--in", dest="src", required=True, help="Входной CSV файл")
    c_xlsx.add_argument("--out", dest="dst", required=True, help="Куда сохранить XLSX")

    opts = parser.parse_args()

    if not os.path.isfile(opts.src):
        raise FileNotFoundError(f"Файл '{opts.src}' не найден")

    if opts.action == "json2csv":
        json_to_csv(opts.src, opts.dst)
    elif opts.action == "csv2json":
        csv_to_json(opts.src, opts.dst)
    elif opts.action == "csv2xlsx":
        csv_to_xlsx(opts.src, opts.dst)
    else:
        parser.error("Неизвестная операция")


if __name__ == "__main__":
    main()
