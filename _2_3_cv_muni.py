
# du_X_Y.py
# Nepovinné úkoly
# Cvičení 2.3: Oblíbené číslo
# Alice, Bob a Cyril si chtějí vybrat společné oblíbené číslo.
# • Alici se líbí dvouciferná čísla, která obsahují čtyřku.
# • Bobovi se líbí čísla dělitelná třemi.
# • Cyrilovi se líbi všechna čísla kromě násobků sedmi.
# Úkol:
# Zjistěte, jestli se zadané přirozené číslo n bude líbit všem třem. Výsledek uložte do
# proměnné all_like. (O vstup a výstup se stará předpřipravený kód.)
# Tip: úkol rozdělte na podúkoly a částečné výsledky si ukládejte do pomocných
# proměnných (např. has_2_digits, bob_likes…).
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# 45 42 12
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3:  
# True False False
# 2
# [ ]: n = int(input()) # vstup
# ...
# print(all_like) # výstu
###################################################################################
import math
#################################################################################
# a, b = [float(x) for x in input().split()] # vstup
vstup = int(input())


def dvojciferne(vstup: int) -> bool:

    cislo = list(str(vstup))
    if len(cislo) == 2:
        return True
    else:
        return False

    
def delitelnetremi(vstup: int) -> bool:

    if vstup % 3 == 0:
        return True
    
    else: 
        return False
    
def nasobkysedmi(vstup: int) -> bool:

    if vstup % 7 != 0:
        return True
    
    else:
        return False
    
delitelnetremi = delitelnetremi(vstup)
print(delitelnetremi)
nasobkysedmi = nasobkysedmi(vstup)
print(nasobkysedmi)
dvojciferne = dvojciferne(vstup)
print(dvojciferne)

def main(delitelnetremi, nasobkysedmi, dvojciferne) -> bool:

    if delitelnetremi == nasobkysedmi == dvojciferne == True:
        return True
    
    else:
        return False

print(main(delitelnetremi, nasobkysedmi, dvojciferne))
     
        





