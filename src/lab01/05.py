fio_input = input()
fio_new = " ".join(fio_input.split())

words = fio_new.split()

initials = "".join([word[0].upper() for word in words])

length = len(fio_new)

print(f"ФИО             : {fio_input}")
print(f"Инициалы        : {initials}.")
print(f"Длина (символов): {length}")
