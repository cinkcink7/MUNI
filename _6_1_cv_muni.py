
# # du_X_Y.py
# Cvičení 6.1: Objem kužele
# Úkol:
# Napište funkci cone_volume, která bere jako parametry poloměr podstavy kužele
# (radius) a jeho výšku (height) a vrací objem kužele. Objem kužele lze spočítat podle
# vzorce:
# 𝑉 = 1
# 3
# 𝜋𝑟2ℎ
# Vzorové volání 1:   Vzorové volání 2:  
# cone_volume(10, 5) cone_volume(1.5, 3.2)
# Vzorový výsledek 1:   Vzorový výsledek 2:  
# 523.5987755982989 7.5398223686155035
# [ ]: def cone_volume(radius: float, height: float) -> float:
# ...
# # print(cone_volume(10, 5))
# # print(cone_volume(1.5, 3.2))

from math import pi


r = 5
h = 10

def objem_kuzele(r: float, h: float)-> float:

    objem  = 1/3 * pi * h *r ** 2

    return objem

print(objem_kuzele(10, 5))

