import json
from .models import Student


def students_to_json(students, path):
    """Записывает список студентов в JSON-файл."""
    if not isinstance(students, list):
        raise TypeError("ожидался список объектов Student")

    data = [s.to_dict() for s in students]

    with open(path, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    """Читает JSON и возвращает список Student."""
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise TypeError("JSON должен содержать список")

    student_list = []

    for d in data:
        if not isinstance(d, dict):
            raise TypeError("элемент списка должен быть объектом")

        # Простая типовая валидация
        if not isinstance(d.get("fio"), str):
            raise TypeError("fio должно быть str")
        if not isinstance(d.get("birthdate"), str):
            raise TypeError("birthdate должно быть str")
        if not isinstance(d.get("group"), str):
            raise TypeError("group должно быть str")
        if not isinstance(d.get("gpa"), (float, int)):
            raise TypeError("gpa должен быть числом")

        # Создание объекта Student
        try:
            student = Student.from_dict(d)
        except Exception:
            raise ValueError("некорректные данные студента")

        student_list.append(student)

    return student_list


if __name__ == "__main__":
    inp = "data2/lab08/students_input.json"
    out = "data2/lab08/students_output.json"

    # читаем
    students = students_from_json(inp)

    # выводим
    print("Загруженные студенты:")
    for st in students:
        print(st)

    # записываем
    students_to_json(students, out)

    print("\nФайл успешно записан:", out)
