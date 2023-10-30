
# du_X_Y.py
# Nepovinné úkoly
# Cvičení 2.1: Obdélník
# V této ukázce si napíšeme program pro výpočet obvodu a povrchu obdélníku:
# Obvod 𝑜 a povrch 𝑆 obdélníku o stranách 𝑎, 𝑏 můžeme spočítat podle vzorců:
# 𝑜 = 2𝑎 + 2𝑏
# 𝑆 = 𝑎𝑏
# Úkol:
# Spočítejte obvod a povrch obdélníku o stranách a, b. Výsledky uložte do proměnných
# o, S.
# (O vstup a výstup se stará předpřipravený kód. Tj. první řádek kódu vám zobrazí
# okénko, do kterého vpíšete vzorový vstup (nebo jiný vstup), a zadané hodnoty se uloží
# do proměnných a, b. Poslední řádek pak vypíše hodnoty o, S. Stačí doplnit výpočet
# mezi tím.)
# Vzorový vstup:
# 4 2.5
# Vzorový výstup:
# o: 13.0 S: 10.0
# [ ]: a, b = [float(x) for x in input().split()] # vstup
# o = ...
# S = ...
# print('o:', o, 'S:', S) # výstup

#########################################################################

def obvod(a: float, b: float) -> float:
    #spocit obvod obdelnika
    o = 2* ( a + b )
    return o

print(obvod(3.5, 5.5))

def obsah(a: float, b: float) -> float:
    #spocit obvod obdelnika
    obsah =  ( a * b )

    return obsah
print(obsah(3.5, 5.5))
vysledek_obsah = obsah(3.5, 25)
print(f"obsah ctyruhelnika je {vysledek_obsah:.2f}")





