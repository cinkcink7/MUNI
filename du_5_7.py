
# du_X_Y.py
# DÚ 5.6: Kombinujeme
# Úkol:
# Ze vstupu načtěte řádek bude obsahující několik celých čísel. Zjistěte, jaké různé
# součty lze získat sčítáním dvojic z těchto čísel.
# Příklad: 8 12 1
# • 8 + 12 = 20
# • 8 + 1 = 9
# • 12 + 1 = 13
# Všechny možné součty vypište na výstup, od nejmenšího po největší. Žádný součet
# nevypisujte dvakrát, ani pokud ho lze získat více různými kombinacemi. Číslo nemůže
# tvořit dvojici samo se sebou, ledaže se na vstupu vyskytuje víckrát.
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# 8 12 1 1 2 2 5 6 7 8 10 -10 -20 0
# 3
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3:  
# 9 13 20 3 4 6 7 8 9 10 11 12 13 14 15 -30 -20 -10 0 10





vstup = input("Zadej celá čísla oddělená mezerami: \n")
cisla = list(map(int, vstup.split()))
# print(cisla)
soucty = set()

for i in range(len(cisla)):
    for j in range(i + 1, len(cisla)):
        soucet = cisla[i] + cisla[j]
        soucty.add(soucet)

vysledky = sorted(list(soucty))

for vysledek in vysledky:
    
    print(vysledek,end = ' ' )
    






























