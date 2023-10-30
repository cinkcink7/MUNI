
# du_X_Y.py

# Povinné domácí úkoly

# DÚ 2.2: Objem kužele
# Úkol:
# Vypočítejte objem kužele s poloměrem podstavy r a výškou v. Výsledek uložte to
# proměnné V.
# 𝑉 = 1
# 3
# ⋅ 𝜋 ⋅ 𝑟2
# ⋅ 𝑣
# Vzorový vstup:
# 3.5 12.0
# 1
# Vzorový výstup:
# 153.94
# [ ]: r, v = [float(x) for x in input().split()] # vstup
# V = ...
# print(f'{V:.2f}') # výstup (na 2 desetinná místa)


# varA

# from math import pi
# # Načtěte čísla od uživatele oddělená mezerami
# cisla = input("Zadej dve čísla oddělená mezerami: ").split()

# # Zkontrolujte, zda uživatel zadal tři čísla
# if len(cisla) != 2:
#     print("Musíte zadat právě dve čísla.")
# else:
#     # Převeďte vstupní řetězce na desetinná čísla
#     r = float(cisla[0])
#     v = float(cisla[1])
    


    

#     # Vypočítejte součet
#     V = 1/3 * pi * (r**2) * v 

#     # Vypište výsledek
#     # print(V)
#     print(f'{V:.2f}') 


#varB

import math

r, v = [float(x) for x in input().split()]
V = (1/3) * math.pi * r**2 * v
print(f'{V:.2f}')



