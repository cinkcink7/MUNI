
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat neakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).


# DÚ 6.3: Sněhulák
# Prasátko Peppa si chce vymodelovat z plastelíny sněhuláka a potřebuje vědet, kolik
# válečků plastelíny si musí koupit.
# Úkol:
# Napište funkci clay_pieces_for_snowman, která bere tři argumenty:
# • snowman_diameters je seznam průměrů jednotlivých koulí sněhuláka (mohou být
# 3 nebo jiný počet),
# • piece_diameter je průměr válečku plastelíny,
# • piece_length je délka válečku plastelíny.
# 2
# Funkce vrátí počet válečků potřebný ke stavbě sněhuláka. Aby funkce nebyla příliš
# složitá, zadefinujte si pomocné funkce (např. na výpočet objemu koule, objemu celého
# sněhuláka, objemu válečku…), které pak můžete volat v hlavní funkci.
# Nápověda: funkce math.ceil() zaokrouhluje nahoru, math.floor() zaokrouhluje
# dolů. Při zápisu vzorců si dejte pozor na rozdíl mezi průměrem a poloměrem.
# Vzorové volání 1:   Vzorové volání 2:  
# clay_pieces_for_snowman([5, 4, 3],
# 2.2, 6.0)
# clay_pieces_for_snowman([3.9,
# 2], 2, 6)
# Vzorový výsledek 1:   Vzorový výsledek 2:  
# 5 2

""" 
from math import ceil, floor, pi


clay_pieces_for_snowman = ([5, 4, 3], 2.2, 6.0)
# 5 2


snowman_diameters = clay_pieces_for_snowman[0] #seznam prumeru snehulaka
piece_diameter = clay_pieces_for_snowman[1]  #je průměr válečku plastelíny
piece_length  = clay_pieces_for_snowman[2] #je délka válečku plastelíny

def clay_pieces_for_snowman(snowman_diameters: list[float], piece_diameter: float, piece_length: float) -> int:

    objem_valecku = ((piece_diameter/2) * (piece_diameter/2)* pi ) * piece_length

    objem_koule_0 = (4/3) * pi * ((snowman_diameters[0])/2) 
    objem_koule_1 = (4/3) * pi * ((snowman_diameters[1])/2)
    objem_koule_2 = (4/3) * pi * ((snowman_diameters[2])/2)

    objem_snehulaka = objem_koule_1 + objem_koule_0 + objem_koule_2

    pocet_potrebneho_objemu = objem_snehulaka // objem_valecku
    pocet_potrebneho_objemu = objem_snehulaka / objem_valecku

    if pocet_potrebneho_objemu <= pocet_potrebneho_objemu:
        
        konecny_pocet_valceku = ceil(pocet_potrebneho_objemu)
    else: 
        konecny_pocet_valceku = floor(pocet_potrebneho_objemu)

    return konecny_pocet_valceku



print(clay_pieces_for_snowman([5, 4, 3], 2.2, 6.0))
# print(clay_pieces_for_snowman([3.9, 2], 2, 6)) """


########################################################################################################

#varB

from math import ceil, floor, pi

clay_pieces_for_snowman_input = ([5, 4, 3], 2.2, 6.0)
# 5 2

snowman_diameters = clay_pieces_for_snowman_input[0]  # seznam prumeru snehulaka
piece_diameter = clay_pieces_for_snowman_input[1]  # je průměr válečku plastelíny
piece_length = clay_pieces_for_snowman_input[2]  # je délka válečku plastelíny

def clay_pieces_for_snowman(snowman_diameters: list[float], piece_diameter: float, piece_length: float) -> int:

    objem_valecku = ((piece_diameter / 2) ** 2 * pi) * piece_length

    if len(snowman_diameters) == 3:
        objem_koule_0 = (4 / 3) * pi * ((snowman_diameters[0] / 2) ** 3)
        objem_koule_1 = (4 / 3) * pi * ((snowman_diameters[1] / 2) ** 3)
        objem_koule_2 = (4 / 3) * pi * ((snowman_diameters[2] / 2) ** 3)
        objem_snehulaka = objem_koule_1 + objem_koule_0 + objem_koule_2

    elif len(snowman_diameters) == 2:
        objem_koule_0 = (4 / 3) * pi * ((snowman_diameters[0] / 2) ** 3)
        objem_koule_1 = (4 / 3) * pi * ((snowman_diameters[1] / 2) ** 3)
        
        objem_snehulaka = objem_koule_1 + objem_koule_0

    elif len(snowman_diameters) == 1:
        objem_koule_0 = (4 / 3) * pi * ((snowman_diameters[0] / 2) ** 3)
        
        objem_snehulaka = objem_koule_0

    elif len(snowman_diameters) == 0:
        objem_koule_0 = (4 / 3) * pi * ((snowman_diameters[0] / 2) ** 3)
        objem_koule_1 = (4 / 3) * pi * ((snowman_diameters[1] / 2) ** 3)
        objem_koule_2 = (4 / 3) * pi * ((snowman_diameters[2] / 2) ** 3)
        objem_snehulaka = (objem_koule_1 + objem_koule_0 + objem_koule_2)*0



    pocet_potrebneho_objemu = objem_snehulaka / objem_valecku

    if pocet_potrebneho_objemu <= 1:  # Pokud je potřeba méně než jeden valeček
        konecny_pocet_valceku = 0
    else:
        konecny_pocet_valceku = ceil(pocet_potrebneho_objemu)

    return konecny_pocet_valceku

# Příklady použití
print(clay_pieces_for_snowman([5, 4, 3], 2.2, 6.0))
print(clay_pieces_for_snowman([3.9, 2], 2, 6))

####################################################################################################

#varB

# from math import ceil, floor, pi

# def clay_pieces_for_snowman(snowman_diameters, piece_diameter, piece_length):
#     objem_valecku = ((piece_diameter / 2) ** 2 * pi) * piece_length

#     objem_snehulaka = 0
#     for diameter in snowman_diameters:
#         objem_koule = (4 / 3) * pi * ((diameter / 2) ** 3)
#         objem_snehulaka += objem_koule

#     pocet_potrebneho_objemu = objem_snehulaka / objem_valecku

#     if pocet_potrebneho_objemu <= 1:  # Pokud je potřeba méně než jeden valeček
#         konecny_pocet_valceku = 0
#     else:
#         konecny_pocet_valceku = ceil(pocet_potrebneho_objemu)

#     return konecny_pocet_valceku

# # Příklady použití
# print(clay_pieces_for_snowman([5, 4, 3], 2.2, 6.0))
# print(clay_pieces_for_snowman([3.9, 2], 2, 6))

#################################################################################################################################

#varC

# from math import ceil, floor, pi

# def clay_pieces_for_snowman(snowman_diameters, piece_diameter, piece_length):
#     objem_valecku = ((piece_diameter / 2) ** 2 * pi) * piece_length

#     objem_snehulaka = 0
#     for diameter in snowman_diameters:
#         if diameter is not None:
#             objem_koule = (4 / 3) * pi * ((diameter / 2) ** 3)
#             objem_snehulaka += objem_koule

#     if objem_snehulaka == 0:
#         return 0  # Pokud objem_snehulaka je stále nula, znamená to, že v seznamu snowman_diameters nebyly žádné platné údaje.

#     pocet_potrebneho_objemu = objem_snehulaka / objem_valecku

#     if pocet_potrebneho_objemu <= 1:  # Pokud je potřeba méně než jeden valeček
#         konecny_pocet_valceku = 0
#     else:
#         konecny_pocet_valceku = ceil(pocet_potrebneho_objemu)

#     return konecny_pocet_valceku

# # Příklady použití
# print(clay_pieces_for_snowman([5, 4, 3], 2.2, 6.0))  # Bude fungovat i s chybějícím údajem v seznamu
# print(clay_pieces_for_snowman([3.9, 2], 2, 6))  # Bude fungovat i s chybějícím údajem v seznamu














