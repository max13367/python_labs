fio = str(input())
inic = ''
len_ = len(fio)

for i in fio:
    if i.isupper():
        inic += i
     

print(f"ФИО             : {fio}")
print(f"Инициалы        : {inic}.")
print(f"Длина (символов): {len_}")