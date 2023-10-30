
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat neakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).


# #DÚ 6.4: Emívulm uktápzop
# Úkol:
# Napište funkci backwards, která vezme jako argument větu a vrátí tuto větu s každým
# slovem pozpátku. Velikost písmen a interpunkci nemusíte řešit (ve větě budou pouze
# malá písmena a mezery).
# Vzorové volání 1:   Vzorové volání 2:  
# backwards('toto je tajná zpráva') backwards('oktásarp appep ícarv redú')
# Vzorový výsledek 1:   Vzorový výsledek 2:  
# 'otot ej ánjat avárpz' 'prasátko peppa vrací úder'
# [ ]: def backwards(sentence: str) -> str:
# ...
# # print(backwards('toto je tajná zpráva'))
# # print(backwards('oktásarp appep ícarv redú'))

#varA

# def backwards(sentence: str) -> str:
#     words = sentence.split()  # Rozdělíme větu na slova pomocí mezery
#     reversed_words = [word[::-1] for word in words]  # Pro každé slovo vezmeme obrácenou kopii
#     reversed_sentence = ' '.join(reversed_words)  # Sestavíme větu z obrácených slov
#     return reversed_sentence

# # Příklady použití
# print(backwards('toto je tajná zpráva'))  # Výstup: 'otot ej ánjat avárpz'
# print(backwards('oktásarp appep ícarv redú'))  # Výstup: 'prasátko peppa vrací úder'

##############################################################################################################

#varB

from math import ceil

def backwards(veta: str) -> str:
    veta = veta.lower()  # Převedení věty na malá písmena
    slova = veta.split()  # Rozdělení věty na slova

    veta_nova = []

    for slovo in slova:
        nove_slovo = []
        for pismeno in slovo:
            nove_slovo.append(pismeno)
        nove_slovo.reverse()
        pozpatku_slovo = ''.join(nove_slovo)
        veta_nova.append(pozpatku_slovo)

    return ' '.join(veta_nova)

# print(backwards("martin nesere v lese-"))
# print(backwards("Emívulm uktápzop martin ne v lese-"))

