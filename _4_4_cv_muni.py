
# # du_X_Y.py
# # Nepovinné úkoly
# Cvičení 4.4: Pyramida
# Úkol:
# Napište kód, který načte ze vstupu přirozené číslo n a znak z a vykreslí na výstup
# n-patrovou pyramidu složenou ze znaku z.
# (Volný prostor zleva pyramidy je vyplněn mezerami, pouze před posledním řádkem
# není žádná mezera. Zprava mezery nemusí být.)
# Vzorový vstup 1:
# 3 i
# Vzorový výstup 1:
# i
# iii
# iiiii
# Vzorový vstup 2:
# 5 *
# Vzorový výstup 2:
# *
# ***
# *****
# *******
# ********


    # varB

n = int(input("Zadejte přirozené číslo n: "))
z = input("Zadejte znak z: ")

# Kontrola, zda bylo zadané přirozené číslo
if n <= 0:
    print("Zadali jste neplatné číslo.")
else:
    for i in range(1, n + 1):
        # Výpočet počtu mezer zleva
        mezery = " " * (n - i)
        
        # Vytvoření řádku pyramidy
        radek = mezery + z * (2 * i - 1)
        
        # Výpis řádku
        print(radek)