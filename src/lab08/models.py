from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    full_name: str
    birth_date: str
    group: str
    gpa: float

    def __post_init__(self):
        # Проверка формата даты
        try:
            datetime.strptime(self.birth_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Некорректный формат даты (нужно YYYY-MM-DD)")

        # Проверка диапазона GPA
        if not isinstance(self.gpa, (float, int)):
            raise TypeError("GPA должен быть числом")

        if not (0 <= float(self.gpa) <= 5):
            raise ValueError("GPA должен быть в диапазоне от 0 до 5")

        self.gpa = float(self.gpa)

    def age(self) -> int:
        """Возвращает количество полных лет."""
        birth = datetime.strptime(self.birth_date, "%Y-%m-%d").date()
        today = date.today()

        years = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            years -= 1

        return years

    def to_dict(self) -> dict:
        """Сериализация объекта в словарь."""
        return {
            "fio": self.full_name,
            "birthdate": self.birth_date,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создание объекта из словаря."""
        return cls(
            full_name=data["fio"],
            birth_date=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self):
        return f"{self.full_name} ({self.group}) — GPA: {self.gpa}"
