from src.lab10.linked_list import SinglyLinkedList


lst = SinglyLinkedList()
print(f"Длина нашего односвязного списка : {len(lst)}")

lst.append(1)
lst.append(2)
lst.prepend(0)
print(f"Наша нынешняя длина списка после добавления элементов : {len(lst)}")
print(f"Односвязанный список : {list(lst)}")

lst.insert(1, 0.5)
print(f"Длина списка после добавления на 1 индекс числа 0.5 : {len(lst)}")
print(f"Односвязанный список : {list(lst)}")

lst.append(52)
print(f"Односвязанный список после добавления числа в конец : {list(lst)}")
print(lst.pretty())
