
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat nejakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).


# DÚ 6.2: Fibonacciho posloupnost
# Fibonacciho posloupnost je nekonečná posloupnost přirozených čísel, která začíná
# čísly 0, 1, a pak každé další číslo je součtem dvou předchozích:
# • 0, 1, 1, 2, 3, 5, 8, 13, 21, …
# Zobecněná Fibonacciho posloupnost se může začínat libovolnými dvěma čísly a pak
# každé další je součtem dvou předchozích, například:
# • 2, 2, 4, 6, 10, 16, 26, 42, ..
# • 1, 10, 11, 21, 32, 53, 85, …
# Úkol:
# Napište funkci, která bere jako parametr číslo n a vrací seznam prvních n prvků Fibonacciho posloupnosti.
# Funkce může být volána také s nepovinným parametrem start (dvojice čísel), který
# určuje první dva prvky zobecněné Fibonacciho posloupnosti.
# Vzorové volání 1:   Vzorové volání 2:  
# fibonacci(8) fibonacci(6, start=(2, 2))
# Vzorový výsledek 1:   Vzorový výsledek 2:  
# [0, 1, 1, 2, 3, 5, 8, 13] [2, 2, 4, 6, 10, 16]
# [ ]: def fibonacci(n: int, start: tuple[int, int] = (0, 1)) -> list[int]:
# ...
# # print(fibonacci(8))
# # print(fibonacci(6, start=(2, 2)))


# def fibonacci(n: int, start: tuple[int, int] = (0, 1)) -> list[int] 

    # n = 8
    # start = (2, 2)


####################################################################      
# def fibonacci(n):
#     start = [0, 1]
#     while len(start) < n:
#         next_number = start[-1] + start[-2]
#         start.append(next_number)
#     return start

# # Vygenerování prvních 8 členů posloupnosti Fibonacci
# prvnich_8_fibonacci = fibonacci(8)
# print(prvnich_8_fibonacci)
        
##########################################################################

def fibonacci(n: int, start: tuple[int, int] = (0, 1)) -> list[int]:

    start = [0, 1]
    for i in range(2, n):
        next_number = start[i - 1] + start[i - 2]
        start.append(next_number)
    return start

# Vygenerování prvních 8 členů posloupnosti Fibonacci
prvnich_8_fibonacci = fibonacci(8)
# print(prvnich_8_fibonacci)
print(fibonacci(8))



##############################################################
def fibonacci(n: int, start: tuple[int, int] = (0, 1)) -> list[int]:

    start = [2, 2]
    for i in range(2, n):
        next_number = start[i - 1] + start[i - 2]
        start.append(next_number)
    return start

# Vygenerování prvních 6 členů posloupnosti Fibonacci
prvnich_6_fibonacci = fibonacci(6)
# print(prvnich_6_fibonacci)
print(fibonacci(6, start=(2, 2)))
