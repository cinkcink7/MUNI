
# du_X_Y.py

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

a, b, c = [float(x) for x in input().split()]
o = a + b + c
print(o)


