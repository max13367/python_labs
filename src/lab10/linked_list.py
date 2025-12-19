from typing import Any, Iterator, Optional


class Node:
    """Узел односвязного списка."""

    __slots__ = ("value", "next")

    def __init__(self, value: Any, next: Optional["Node"] = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список."""

    __slots__ = ("head", "tail", "_size")

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node  # type: ignore
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        self.head = Node(value, self.head)
        if self._size == 0:
            self.tail = self.head
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next  # type: ignore

        current.next = Node(value, current.next)  # type: ignore
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            self.head = self.head.next  # type: ignore
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        prev = self.head
        for _ in range(idx - 1):
            prev = prev.next  # type: ignore

        if prev.next is self.tail:
            self.tail = prev
        prev.next = prev.next.next  # type: ignore
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"

    def pretty(self) -> str:
        parts = []
        current = self.head
        while current:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
