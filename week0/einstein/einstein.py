# References: https://docs.python.org/3/library/functions.html#pow


def main():
    mass = int(input("m: "))
    print(f"E: {energy(mass)}")


# Calculates the equivalent energy of a matter in Joules
def energy(m: float, c: float=300000000) -> float:
    """
    m: mass of matter
    c: speed of light
    """
    return m * pow(c, 2)


main()
