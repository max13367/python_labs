def format_record(student, gruppa, gpa):
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


print(format_record("Иванов Иван Иванович", "BIVT-25", 4.6))
print(format_record("Петров Пётр", "IKBO-12", 5.0))
print(format_record("Петров Пётр Петрович", "IKBO-12", 5.0))
print(format_record("  сидорова  анна   сергеевна ", "ABB-01", 3.999))
