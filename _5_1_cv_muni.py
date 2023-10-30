
# # du_X_Y.py
# # Nepovinné úkoly
# Cvičení 5.1: Převrácené pořadí
# Úkol:
# Napište program, který bude od uživatele načítat řádky textu až do chvíle, 
#kdy uživatel zadá prázdný řádek. Poté program vypíše všechny doposud zadané řádky, ale v
# opačném pořadí.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 1 v případě potřeby je možné
# 2 se seznámit s projektem
# 3 technické podpory a spolupráce
# s rozvojovými zeměmi na podlaze a
# zabývali se také podílí
# na předním sedadle
# Vzorový výstup 1:   Vzorový výstup 2:  
# 3 na předním sedadle
# 2 zabývali se také podílí
# 1 s rozvojovými zeměmi na podlaze a
# technické podpory a spolupráce
# se seznámit s projektem
# v případě potřeby je možné
# print(vystup)



vstup_list = []

def krmic():
    # bud krmit radkaz dokud nenarazi na nevyplneny radek
    
    while True:
        vstup = input()

        if len(vstup) == 0:
            return vstup_list
        else: 
            vstup_list.append(vstup)

vysledek_krmic = (krmic())
revesni_list_krmic = vysledek_krmic[::-1]
vystup = "\n".join(map(str, revesni_list_krmic)) # vypise to jako str polozku na kazdy radek zvlast
print(vystup)