
# du_X_Y.py
# DÚ 4.5: Půlení
# Úkol:
# Ze vstupu načtěte přirozené číslo. Zjistěte kolikrát po sobě lze toto číslo dělit dvěma
# (např. 80 -> 40 -> 20 -> 10 -> 5, odpověď je 4krát).
# Vzorový vstup 1:   Vzorový vstup 2:  
# 80 9
# Vzorový výstup 1:   Vzorový výstup 2:  
# 4 0

# DÚ 5.1: Popelka
# Úkol:
# Na vstupu získate řádek s přirozenými čísly. Roztřiďte je a vypište lichá zvlášť, sudá
# zvlášť.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 8 11 4 3 7 2 6 13 5 12 9
# Vzorový výstup 1:   Vzorový výstup 2:  
# Lichá: 11 3 7 13 5 Lichá: 9
# Sudá: 8 4 2 6 12 Sudá

# vstup = 8 11 4 3 7 2 6 13 5 12 9
vstup = input("Zadej sadu prirozenych cisel: \n")
vstup = vstup.split()
# print(vstup)

suda = []
licha = []

for i in vstup:
    i = int(i)
    
    if i % 2 == 0:
        suda.append(i)
    else: 
        licha.append(i)

# print(suda)
# print(licha)
licha_string = ' '.join(map(str, licha))
print(f"Licha: {licha_string}")
suda_string = ' '.join(map(str, suda))
print(f"Suda: {suda_string}")











