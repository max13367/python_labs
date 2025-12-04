import json
from pathlib import Path
import csv
import pytest


from src.lab05.json_csv import json_to_csv, csv_to_json


# ------------------------- JSON → CSV -------------------------


def test_json_to_csv_success(tmp_path):
    """Корректный JSON → корректный CSV"""
    source_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "London"},
    ]

    src = tmp_path / "src.json"
    dst = tmp_path / "result.csv"

    src.write_text(
        json.dumps(source_data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    json_to_csv(str(src), str(dst))
    assert dst.exists()

    with open(dst, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert rows[0]["name"] == "Alice"
    assert rows[0]["age"] == "30"
    assert rows[0]["city"] == "New York"
    assert rows[1]["name"] == "Bob"


def test_json_to_csv_nonexistent():
    """Ошибка: входной файл не существует"""
    with pytest.raises(FileNotFoundError):
        json_to_csv("missing_file.json", "out.csv")


def test_json_to_csv_broken_json(tmp_path):
    """Ошибка: JSON повреждён"""
    p = tmp_path / "invalid.json"
    p.write_text("{ broken json }", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(p), "output.csv")


# ------------------------- CSV → JSON -------------------------


def test_csv_to_json_success(tmp_path):
    csv_data = [
        ["name", "age", "city"],
        ["Alice", "30", "New York"],
        ["Bob", "25", "London"],
    ]

    src = tmp_path / "src.csv"
    dst = tmp_path / "res.json"

    with open(src, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)

    csv_to_json(str(src), str(dst))
    assert dst.exists()

    with open(dst, encoding="utf-8") as f:
        parsed = json.load(f)

    assert len(parsed) == 2
    assert parsed[0] == {"name": "Alice", "age": "30", "city": "New York"}


def test_csv_to_json_missing_file():
    with pytest.raises(FileNotFoundError):
        csv_to_json("not_exists.csv", "result.json")


def test_csv_to_json_invalid(tmp_path):
    """Ошибка: пустой CSV"""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(csv_file), "output.json")
