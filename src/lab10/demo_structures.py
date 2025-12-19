from src.lab10.structures import Stack, Queue


print("1. Создан стек:")
stack = Stack()
print(f"   Пустой? {stack.is_empty()}, Длина: {len(stack)}, Верх: {stack.peek()}")

elements = [10, 20, 30, "текст", [1, 2]]
for elem in elements:
    stack.push(elem)
    print(f"2. Добавили {elem}: {stack}")
    print(f"   Верхний: {stack.peek()}, Длина: {len(stack)}")

print("\n3. Извлекаем (LIFO порядок):")
while not stack.is_empty():
    item = stack.pop()
    print(f"   Извлекли: {item}, Осталось: {len(stack)}, Верх: {stack.peek()}")

print(f"\n4. Итог: {stack}, Пустой? {stack.is_empty()}\n")


print("1. Создана очередь:")
queue = Queue()
print(f"   Пустая? {queue.is_empty()}, Длина: {len(queue)}, Первый: {queue.peek()}")

elements = ["первый", "второй", "третий", 100, 200]
for elem in elements:
    queue.enqueue(elem)
    print(f"2. Добавили {elem}: {queue}")
    print(f"   Первый: {queue.peek()}, Длина: {len(queue)}")

print("\n3. Извлекаем (FIFO порядок):")
while not queue.is_empty():
    item = queue.dequeue()
    print(f"   Извлекли: {item}, Осталось: {len(queue)}, Первый: {queue.peek()}")

print(f"\n4. Итог: {queue}, Пустая? {queue.is_empty()}")
