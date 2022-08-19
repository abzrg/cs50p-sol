class Wizzard:
    def __init__(self, name: str):
        if not name:
            raise ValueError("Missing Name")
        self.name = name

    ...


class Student(Wizzard):
    def __init__(self, name: str, house: str):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizzard):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject

    ...


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
