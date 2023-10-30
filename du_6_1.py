
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat nejakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).
# DÚ 6.1: Vzdálenost bodů
# Mějme dva body v rovině: 𝐴 = [𝑎𝑥
# , 𝑎𝑦
# ], 𝐵 = [𝑏𝑥
# , 𝑏𝑦
# ].
# Vzdálenost mezi body 𝐴, 𝐵 umíme spočítat podle vzorce:
# |𝐴𝐵| = √(𝑎𝑥 − 𝑏𝑥
# )
# 2 + (𝑎𝑦 − 𝑏𝑦
# )
# 2
# Úkol:
# Napište funkci distance, která bere jako parametry souřadnice dvou bodů v rovině
# (tj. dvě dvojice reálných čísel) a vrací vzdálenost těchto bodů.
# Vzorové volání 1:   Vzorové volání 2:  
# distance((1, 1), (5, 4)) distance((-1.5, 3.2), (5.8, 12.6))
# Vzorový výsledek 1:   Vzorový výsledek 2:  
# 5.0 11.901680553602503


# import math
# def distance(bod_a: tuple[float, float], bod_b:tuple[float, float]):
#     #tato fnc meri vzdalenost bodu a,b

#     bod_a = [1, 1]
#     bod_b = [5, 4]

#     x = ((bod_a[0]) - (bod_b[0]))**2
#     print(x)
#     y= ((bod_a[1])**2 - (bod_b[1]))**2
#     print(y)
#     abs_distance = (abs(x + y))
#     distance = math.sqrt(abs_distance)
#     return distance

# print(distance([1,1], [5,4]))

#######################################################################    
####VarB
# import math



# def distance(bod_a: tuple[float, float], bod_b:tuple[float, float]) -> float:
#     #tato fnc meri vzdalenost bodu a,b

#     # bod_a = [1, 1]
#     # bod_b = [5, 4]

#     x = ((bod_a[0]) - (bod_b[0]))**2
#     print(x)
#     y= ((bod_a[1])**2 - (bod_b[1]))**2
#     print(y)
#     abs_distance = (abs(x + y))
#     distance = math.sqrt(abs_distance)

#     return distance

# print(distance([1,1], [5,4]))

#######################################################################
####VarC


import math

def distance(point1: tuple[float, float], point2: tuple[float, float]) ->float:
    return math.dist(point1, point2)

# Vzorová volání:
vzdalenost1 = distance((1, 1), (5, 4))
vzdalenost2 = distance((-1.5, 3.2), (5.8, 12.6))

print(vzdalenost1)  # Vzorový výsledek 1: 5.0
print(vzdalenost2)  # Vzorový výsledek 2: 10.442548329704964