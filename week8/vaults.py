class Vault:
    def __init__(self, galleons: int, sickles: int, knuts: int):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other: 'Vault') -> 'Vault':
        galleons: int = self.galleons + other.galleons
        sickles: int = self.sickles + other.sickles
        knuts: int = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)



def main() -> int:
    harry: Vault = Vault(100, 50, 75)
    ali: Vault = Vault(250, 25, 50)
    total: Vault = ali + harry
    print(total)
    input()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
