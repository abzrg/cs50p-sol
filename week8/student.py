"""Student Class Demo"""

class Student:
    """Student Class"""
    def __init__(self, name: str, house: str,) -> None:
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        """Gets a students from stdin"""
        name: str = input("Name: ")
        house: str = input("House: ")
        return cls(name, house)

    @property
    def name(self):
        """Getter for name attribute"""
        return self._name

    @name.setter
    def name(self, name: str):
        """Setter for name attribute"""
        if not name:
            raise ValueError("Missing name")
        self._name: str = name

    @property
    def house(self):
        """Getter for house attribute"""
        return self._house

    @house.setter
    def house(self, house: str):
        """Setter for house attribute"""
        if house not in ["Gryffindor", "Huffelpuf", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house: str = house


def main() -> int:
    """Main function"""
    student = Student.get()
    print(f"{student.name} from {student.house}")
    input()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
