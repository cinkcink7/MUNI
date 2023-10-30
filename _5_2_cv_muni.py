
# # du_X_Y.py
# # Nepovinné úkoly
# Cvičení 5.2: Slovník
# Na vstupu získáte dvojice klic=hodnota. Vytvořte z nich slovník a vypište ho na
# výstup.
# Vzorový vstup:
# pondělí=řízek úterý=smažák středa=halušky čtvrtek=guláš pátek=smažák
# 1
# Vzorový výstup:
# {'pondělí': 'řízek', 'úterý': 'smažák', 'středa': 'halušky', 'čtvrtek':
# 'guláš', 'pátek': 'smažák'}


vstup = input()
vstup = vstup.split() #tvorim lsit

slovnik = {}

for item in vstup:

    klic, hodnota = item.split('=')

    slovnik[klic] = hodnota

print(slovnik)

