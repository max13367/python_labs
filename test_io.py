# test_io.py
from src.lab04.io_txt_csv import read_text, write_csv


txt = read_text("data/lab04/input.txt")
print("Прочитанный текст:")
print(repr(txt))
print(f"Длина текста: {len(txt)} символов")


write_csv([("word","count"),("test",3)], "data/lab04/check.csv")
print("CSV файл создан: data/lab04/check.csv")

# Проверим содержимое
with open("data/lab04/check.csv", "r", encoding="utf-8") as f:
    print("Содержимое CSV:")
    print(f.read())