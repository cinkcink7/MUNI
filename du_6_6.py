
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat neakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).


# DÚ 6.6: Modus
# Modus (anglicky mode) je hodnota, která se v daném statistickém souboru vyskytuje
# nejčastěji. Obecně může mít soubor i víc modů, pokud je v něm víc různých hodnot
# 4
# se stejným počtem výskytů.
# Úkol:
# Napište definici funkce mode, která bere seznam a vrací jeho modus. Pokud bude
# seznam prázdný, vraťte None. Pokud bude víc modů, vraťte jeden z nich – je jedno
# který.
# Vzorové volání 1:
# mode([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2])
# Vzorový výsledek 1:
# 2
# Vzorové volání 2:
# mode(['jablko', 'pomeranč', 'hruška', 'pomeranč', 'jablko', 'jablko',
# 'hruška'])
# Vzorový výsledek 2:
# 'jablko'
# [ ]: def mode(elements: list[object]) -> object:
# ...
# # print(mode([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]))
# # print(mode(['jablko', 'pomeranč', 'hruška', 'pomeranč', 'jablko',␣
# ↪'jablko', 'hruška']))
##################################################################################################



#varA:

# from collections import Counter

# def mode(elements: list[object]) -> object:
#     if not elements:
#         return None
    
#     counts = Counter(elements)
#     max_count = max(counts.values())
#     modes = [key for key, value in counts.items() if value == max_count]
    
#     return modes[0]

# # Příklady použití
# print(mode([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]))
# print(mode(['jablko', 'pomeranč', 'hruška', 'pomeranč', 'jablko', 'jablko', 'hruška']))

############################################################################################################

# #varB

# def mode(elements: list[object]) -> object:
#     if not elements:
#         return None

#     # Vytvoříme slovník, kde klíče budou prvky ze vstupního seznamu a hodnoty budou četnosti těchto prvků.
#     counts = {}
#     for item in elements:
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1

#     # Najdeme maximum v počtech výskytů.
#     max_count = max(counts.values())

#     # Zjistíme, které prvky mají tento počet výskytů (mohou být více modů).
#     modes = [key for key, value in counts.items() if value == max_count]

#     # Vrátíme jeden z prvků, které jsou modem.
#     return modes[0]



# # Příklady použití


# print(mode(['jablko', 'pomeranč', 'hruška', 'pomeranč', 'jablko', 'jablko', 'hruška']))
# print(mode([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]))
# print(mode([]))
#################################################################

#varC

def mode(elements: list[object]) -> object:
    if not elements:
        return None

    # Vytvoříme slovník, kde klíče budou prvky ze vstupního seznamu a hodnoty budou četnosti těchto prvků.
    counts = {}
    for item in elements:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # Najdeme maximum v počtech výskytů.
    max_count = max(counts.values())

    # Zjistíme, které prvky mají tento počet výskytů (mohou být více modů).
    modes = [key for key, value in counts.items() if value == max_count]

    # Vrátíme jeden z prvků, které jsou modem.
    return modes[0]

# Příklady použití
print(mode([1, 2, 3, 3, 4, 4, 1, 2, 5, 3, 2, 1, 2]))
print(mode(['jablko', 'pomeranč', 'hruška', 'pomeranč', 'jablko', 'jablko', 'hruška']))  # Vrací 'jablko'
print(mode([]))
print(mode([11, 55, 55, 11]))



















