"""
Opravte chyby v tomto programu. Pomozte si modulem mypy (typové anotace v tomto programu nejsou nutně správné).

Zadání: 
Roztřiď čísla ze vstupu na sudá a lichá a vypiš každé zvlášť.
"""
def select_even(numbers: list[int]) -> list[int]:
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result


def select_odd(numbers: list[int]) -> list[int]:
    result = []
    for x in numbers:
        if x % 2 != 0:  # Oprava pro výběr lichých čísel
            result.append(x)
    return result


def main() -> None:
    numbers = list(map(int, input('Input numbers: ').split()))

    even_numbers = select_even(numbers)
    odd_numbers = select_odd(numbers)
    
    print('Even numbers:', ', '.join(map(str, even_numbers)))
    print('Odd numbers:', ', '.join(map(str, odd_numbers)))


if __name__ == '__main__':
    main()


