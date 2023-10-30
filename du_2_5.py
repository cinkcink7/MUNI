
# du_X_Y.py

# DÚ 2.5: Různá čísla?
# Úkol:
# V proměnných x, y, z máme uložena 3 reálná čísla. Rozhodněte zda každé z těchto
# čísel je jiné a výsledek (logickou hodnotu) uložte do proměnné are_distinct.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 15.0 3.14 100 0.5 -9.5 0.5
# Vzorový výstup 1:   Vzorový výstup 2:  
# True False
# [ ]: x, y, z = [float(x) for x in input().split()] # vstup
# ...
# print(are_distinct) # výstu
#  varA
# x = float(input("Zadej první číslo: "))
# y = float(input("Zadej druhé číslo: "))
# z = float(input("Zadej třetí číslo: "))

# # Porovnej čísla a zkontroluj, zda jsou všechna různá
# are_distinct = x != y and x != z and y != z

# # Výstup v závislosti na výsledku
# if are_distinct:
#     print(True)
# else:
#     print(False)
  

# var B:


x, y, z = [float(x) for x in input().split()]

# Porovnává, zda jsou tři čísla různá
are_distinct = x != y and x != z and y != z

print(are_distinct)
