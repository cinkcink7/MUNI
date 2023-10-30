
# du_X_Y.py
# DÚ 4.5: Půlení
# Úkol:
# Ze vstupu načtěte přirozené číslo. Zjistěte kolikrát po sobě lze toto číslo dělit dvěma
# (např. 80 -> 40 -> 20 -> 10 -> 5, odpověď je 4krát).
# Vzorový vstup 1:   Vzorový vstup 2:  
# 80 9
# Vzorový výstup 1:   Vzorový výstup 2:  
# 4 0


# cislo = int(input("Zadej přirozené číslo: "))
# pocet_deleni = 0

# while cislo > 1:
#     if cislo % 2 == 0:
#         cislo = cislo // 2
#         pocet_deleni += 1
#     else:
#         break

# print("Počet dělení dvěma:", pocet_deleni)

###################################################################################


# var b

# Načtěte přirozené číslo ze vstupu
cislo = int(input("Zadej přirozené číslo: "))

# Inicializujte proměnnou pro počet dělení
pocet_deleni = 0

# Počítejte, kolikrát lze číslo dělit dvěma
while cislo > 1:
    if cislo % 2 == 0:
        cislo = cislo // 2
        pocet_deleni += 1
    else:
        break

# Vypište počet dělení dvěma
print(pocet_deleni)












