# Math interpreter



def main():
    statement = input("> ")
    print(intrprt(statement))


def intrprt(statement: str) -> int:
    lhs, op, rhs = statement.strip().split()

    if op == "+":
        return float(lhs) + float(rhs)
    elif op == "-":
        return float(lhs) - float(rhs)
    elif op == "/":
        return float(lhs) / float(rhs)
    elif op == "*":
        return float(lhs) * float(rhs)
    else:
        return None


main()
