
# du_X_Y.py

# DÚ 2.3: Pythagorova věta
# Úkol:
# Vypočítejte délku přepony c pravoúhlého trojúhelníku z délek odvěsen a, b podle
# Pythagorovy věty:
# 𝑎
# 2 + 𝑏2 = 𝑐2
# Vzorový vstup:
# 3.82 3.56

# varA:

# from math import pi, sqrt
# # Načtěte čísla od uživatele oddělená mezerami
# cisla = input("Zadej dve čísla oddělená mezerami: ").split()

# # Zkontrolujte, zda uživatel zadal tři čísla
# if len(cisla) != 2:
#     print("Musíte zadat právě dve čísla.")
# else:
#     # Převeďte vstupní řetězce na desetinná čísla
#     a = float(cisla[0])
#     b = float(cisla[1])
    
#     # Vypočítejte součet
#     c = sqrt(a**2 + b**2)

#     # Vypište výsledek
    
#     print(f'{c:.2f}') 

# varB:
import math

a, b = [float(x) for x in input().split()]
c = math.sqrt(a**2 + b**2)
print(f"{c:.2f}")

