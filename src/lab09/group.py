import csv
from pathlib import Path
from models import Student


class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Создаёт CSV с заголовком, если он отсутствует."""
        if not self.path.parent.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)

        if not self.path.exists():
            with open(self.path, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _read_all(self):
        """Чтение всех строк CSV."""
        students = []

        with open(self.path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row:
                    students.append(row)

        return students

    def _ensure_storage_exists(self, students: list):
        """Перезапись CSV."""
        with open(self.path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(students)

    def list(self):
        return self._read_all()

    def add(self, student: Student):
        students = self._read_all()

        students.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": student.gpa,
        })

        self._ensure_storage_exists(students)

    def find(self, substr: str):
        rows = self._read_all()
        return [r for r in rows if substr.lower() in r["fio"].lower()]

    def remove(self, fio: str):
        rows = self._read_all()

        new_rows = [r for r in rows if r["fio"] != fio]

        if len(new_rows) == len(rows):
            return False

        self._ensure_storage_exists(new_rows)
        return True

    def update(self, fio: str, **fields):
        rows = self._read_all()
        updated = False

        for row in rows:
            if row["fio"] == fio:
                for k, v in fields.items():
                    row[k] = v
                updated = True

        if updated:
            self._ensure_storage_exists(rows)

        return updated

    @staticmethod
    def find_max(array):
        if not array:
            return None
        return max(array)

    @staticmethod
    def find_min(array):
        if not array:
            return None
        return min(array)


    def stats(self):
        students = self._read_all()

        if not students:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": 0,
                "groups": {},
                "top_5": []
            }

        gpas = [float(s["gpa"]) for s in students]
        groups = [s["group"] for s in students]
        group_count = {g: groups.count(g) for g in set(groups)}

        top_5 = sorted(students, key=lambda s: float(s["gpa"]), reverse=True)[:5]
        top_5_list = [{"fio": s["fio"], "gpa": float(s["gpa"])} for s in top_5]

        return {
            "count": len(students),
            "min_gpa": self.find_min(gpas),
            "max_gpa": self.find_max(gpas),
            "avg_gpa": round(sum(gpas) / len(students), 3),
            "groups": group_count,
            "top_5": top_5_list,
        }



# Тесты

people = Group("../../data2/lab09/students.csv")


#print(people.list())

#people.add(Student("Батраченко Максим Иванович", "2007-06-18", "БИВТ-25-7", 4.6))

#print(people.find("Макс"))

#people.remove("Батраченко Максим Иванович")

#people.update("Попов Сергей Михайлович", gpa="5.0")

#print(people.stats())
