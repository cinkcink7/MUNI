
# du_X_Y.py

# Povinné domácí úkoly
# Povinné domácí úkoly
# DÚ 2.1: Obvod trojúhelníku
# Úkol:
# Vypočítejte obvod trojúhelníku se stranami o délkách a, b, c. Výsledek uložte do
# proměnné o.
# Vzorový vstup:
# 2 3 4
# Vzorový výstup:
# 9.0
# [ ]: a, b, c = [float(x) for x in input().split()] # vstup
# o = ...
# print(o) # výstup

#varA

# a = float(input("Zadej a:"))
# b = float(input('Zadej b:'))
# c = float(input("Zadej c:"))

def fibonacci(n: int) -> list[int]:
    """Spočítej prvních n prvků Fibonacciho posloupnosti."""
    x = []
    a = 0
    b = 1
    for a in range(n):
        x.append(b)
        c = a + b
        a = b
        b = c
    return(x) # chybne odsazeni bylo mimo fnc


def print_fibonacci() -> None:
    """Vypiš uživatelem zadaný počet prvků Fibonacciho posloupnosti."""
    n = int(input('Zadej požadovaný počet prvků Fibonacciho posloupnosti: ')) # prava z N na n

    #doctest c_1
    """>>> n = 4
    [1, 1, 2, 4]
    """

    # doctest c_2
    """>>> n = "a"
    VallueError
    """
    # doctest c_3
    """>>> n = -1
    "letadlo"
    """
    print(fibonacci(n))


if __name__ == '__main__':
    print_fibonacci()