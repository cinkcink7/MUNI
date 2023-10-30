
# # du_X_Y.py
# Cvičení 6.2: Dělitelé
# Úkol:
# Napište funkci divisors, která bere jako parametr přirozené číslo n a vrací seznam
# všech dělitelů čísla n (v pořadí od nejmenšího).
# Funkce navíc bere nepovinný parametr proper:
# • Pokud je proper nastaveno na False (default), pak funkce vrací všechny dělitele,
# včetně samotného n.
# • Pokud je proper nastaveno na True, pak funkce vrací pouze vlastní dělitele, tj.
# všechny dělitele kromě samotného n.
# Poznámka: na hledání dělitelů existují efektivnější algoritmy, ale v této úloze úplně
# postačí naivní řešení, tj. zkusit všechna čísla od 1 až po n.
# Vzorové volání 1:   Vzorové volání 2:  
# divisors(12) divisors(30, proper=True)
# Vzorový výsledek 1:   Vzorový výsledek 2:  
# [1, 2, 3, 4, 6, 12] [1, 2, 3, 5, 6, 10, 15]
# [ ]: def divisors(n: int, proper: bool = False) -> list[int]:
# ...
# # print(divisors(12))
# # print(divisors(30, proper=True))

cislo = 36


def hledac_delitelu(cislo):
    # najde vsechny delitele cisla
    vystup = []
    for i in range(1, cislo):

        if cislo % (i) == 0:
           vystup.append(i)

    return vystup

print(hledac_delitelu(cislo))

