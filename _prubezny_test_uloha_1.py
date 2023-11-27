# print("Hallo World!")
# du_X_Y.py


# Pokyny:
# • Během testu je povoleno používat libovolné materiály vč. internetu. Zakázána
# je pouze komunikace (online i fyzická) s jiným člověkem (kromě učitele).
# • Na řešení testu jsou vyhrazeny 2 hodiny, lze získat maximálně 50 bodů.
# • Řešení je nutné vyplnit:
# – Přímo do tohoto souboru prubezny_test.ipynb (a testy si spustit pomocí
# testovacích buněk)
# – Nebo každý úkol zvlášť do souborů prubezny_?.py, kde ? je číslo úkolu (a
# testy si spustit z příkazového řádku: python testing.py prubezny_?.py).
# • Pozor, úkoly jsou dvou typů:
# – Napsat program: je třeba načítat vstup pomocí input a vypsat výstup pomocí print. V zadání je uveden vzorový vstup a vzorový výstup.
# – Napsat funkci: není třeba načítat vstup (vstupní data budou předána
# v parametrech funkce), výsledek má být vrácen jako návratová hodnota
# funkce (return). V zadání je uvedeno vzorové volání a vzorový výsledek.
# Typové anotace v šablonách funkcí považujte za součást zadání.
# • Řešení odevzdejte včas do připravené odevzdávárny.
# Úkol 1 (12 bodů)
# Napište program, který ze vstupu načte řádek s názvy krajů a jejich počty obyvatel.
# Program pak vypíše na výstup tabulku, ve které bude pro každý kraj:
# • název (zarovnaný doleva na 15 znaků)
# • počet obyvatel (zarovnaný doprava na 7 znaků)
# • grafické znázornění počtu obyvatel (každých celých 100 000 obyvatel = jeden
# znak &)
# Jednotlivé sloupce jsou oddělené dvěma mezerami.
# Vzorový vstup:
# 1
# Jihočeský: 643551, Jihomoravský: 1195327, Karlovarský: 293311,
# Královéhradecký: 550803, Liberecký: 442476, Moravskoslezský: 1192834,
# Olomoucký: 630522, Pardubický: 522856, Plzeňský: 591041, Praha:
# 1335084, Středočeský: 1397997, Ústecký: 817004, Vysočina: 508852,
# Zlínský: 580119
# Vzorový výstup:
# Jihočeský 643551 &&&&&&
# Jihomoravský 1195327 &&&&&&&&&&&
# Karlovarský 293311 &&
# Královéhradecký 550803 &&&&&
# Liberecký 442476 &&&&
# Moravskoslezský 1192834 &&&&&&&&&&&
# Olomoucký 630522 &&&&&&
# Pardubický 522856 &&&&&
# Plzeňský 591041 &&&&&
# Praha 1335084 &&&&&&&&&&&&&
# Středočeský 1397997 &&&&&&&&&&&&&
# Ústecký 817004 &&&&&&&&
# Vysočina 508852 &&&&&
# Zlínský 580119 &&&&&

# varA


vstup = input("Vstup: \n")
kraje = vstup.split(",")
# print(vstup)

data_kraju = {}
for kraj in kraje:
    nazev, pocet_obyvatel = kraj.split(': ')
    data_kraju[nazev] = int(pocet_obyvatel)

for kraj, pocet in data_kraju.items():
    graficky_znac = '&' * (pocet // 1000)  # Používáme // místo / pro celočíselné dělení
    # Výpis kraje, počtu obyvatel a grafického znázornění
    print(f'{kraj.ljust(15)}{str(pocet).rjust(7)}  {graficky_znac}')






#############################################################################################################


# # varB
# # Načtení vstupu
# vstup = input()

# # Rozdělení vstupního řádku na jednotlivé kraje
# kraje = vstup.split(', ')

# # Inicializace prázdného slovníku pro ukládání dat o krajích
# data_kraju = {}

# # Procházení jednotlivých krajů a jejich počtu obyvatel
# for kraj in kraje:
#     nazev, pocet_obyvatel = kraj.split(': ')
#     data_kraju[nazev] = int(pocet_obyvatel)

# # Výstup
# for kraj, pocet in data_kraju.items():
#     # Vytvoření řetězce pro grafické znázornění počtu obyvatel
#     graficky_znac = '&' * (pocet // 100000)
#     # Výpis kraje, počtu obyvatel a grafického znázornění
#     print(f'{kraj.ljust(15)}{str(pocet).rjust(7)}  {graficky_znac}')
