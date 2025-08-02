from typing import Set, List


def calculate(input: str) -> int:
    """
    convert input into postfix notation: A + B * C --> A B C * +
    by storing operands in one stack and operators in another stack
    and pop values from both in sequence.
    """
    check_operators: Set[str] = set(["+", "-"])
    for op in check_operators:
        input = input.replace(f"{op}", f" {op} ")
    check_parenthesis: Set[str] = set(["(", ")"])
    for op in check_parenthesis:
        input = input.replace(f"{op}", f" {op} ")
    input_split = input.split()  # splits by whitespace
    print(input_split)

    operands: List[int] = []
    operators: List[str] = []
    for character in input_split:
        if character in check_parenthesis:
            continue
        if character in check_operators:
            operators.append(character)
        else:
            if not character.isnumeric():
                raise ValueError(
                    f"Unknown or invalid character found in input: ", character
                )
            operands.append(int(character))
    operands_str = " ".join([str(x) for x in operands])
    operators_str = " ".join(operators)
    print(f"{operands_str} {operators_str}")

    result = operands.pop(0)
    for op in reversed(operators):
        curr = operands.pop()
        if op == "+":
            print(f"{curr} + {result} = {result + curr}")
            result += curr
        elif op == "-":
            print(f"{curr} - {result} = {result - curr}")
            result -= curr
    return result
