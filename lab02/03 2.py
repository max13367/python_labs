def format_record(rec: tuple[str, str, float]) -> str:
    student, gruppa, gpa = rec

    student = ' '.join(student.split()).title()

    parts = student.split()
    familiya = parts[0]


    initial = []
    for i in range(1, len(parts)):
        if parts[i]:
            initial.append(parts[i][0] + '.')

    initials_str = ''.join(initial)


    fio = f'{familiya} {initials_str}, гр. {gruppa.strip()}, GPA {gpa:.2f}'
    return fio


# Тестирование
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))