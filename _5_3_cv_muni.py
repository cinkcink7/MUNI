
# # du_X_Y.py
# Cvičení 5.3: Množina písmen
# Úkol:
# Na vstupu získáte jeden řádek textu, který může obsahovat písmena anglické abecedy,
# číslice a jiné speciální znaky. Vypište na výstup všechna písmena, která se v textu
# vyskytují, bez ohledu na velikost (A/a) a počet výskytů. Písmena vypisujte vždy velká,
# v abecedním pořadí.
# Hint: ve znakové sadě Unicode jdou písmena anglické abecedy za sebou podle
# abecedy (nejdřív velká písmena A–Z s ordinálními čísly 65–90, pak malá písmena a–z s
# čísly 97–122). Porovnávání řetězců funguje na základě ordinálních čísel, např. 'A' <
# 'B' < 'C' < 'Z' < 'a' < 'b' < 'c' < 'z' < 'ý' < 'ň' (pro písmena s diakritikou toto hezké uspořádání už bohužel neplatí). Stejný princip používají například i
# funkce min, max, sorted.
# Vzorový vstup 1:   Vzorový vstup 2:  
# And I meant it! !@#$%^&*(123)
# Vzorový výstup 1:   Vzorový výstup 2:  
# ADEIMNT
# [ ]: ...
# # Vzorové vstupy pro kopírování:
# # And I meant it!
# # !@#$%^&*(123
# varA
# vstup = input()  # Přečteme vstupní řádek textu

# # Inicializace množiny pro ukládání písmen
# pismena = set()

# for znak in vstup:
#     if znak.isalpha():  # Kontrola, zda je znak písmeno
#         pismena.add(znak.upper())  # Přidáme písmeno (ve formě velkých písmen) do množiny

# # Seřadíme písmena v abecedním pořadí a převedeme je na řetězec
# vystup = ''.join(sorted(pismena))

# print(vystup)  # Vypíšeme všechna písmena (velká) v abecedním pořadí
###########################################################################################################################


# varBv # kdzy to drbes ...


# vstup = input()
# text = vstup.upper()
# # unicode_unicod_slovnik = {}

# def unicod_slovnik_unicode():
#  #ffdela to unicode unicod_slovnik a vraci ho

#     unicode_unicod_slovnik = {}

#     for znak in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
#         unicode_hodnota = ord(znak)
#         unicode_unicod_slovnik[znak] = unicode_hodnota

#     return unicode_unicod_slovnik
# #print(unicod_slovnik_unicode())


# def transformace_t_na_u(vstup, unicode_unicod_slovnik):
# #transformuje text na unicod .. zde vstup transformuje na jeho cisla
#     list_vstup = []
#     for i in vstup:  # i jsou pismenka

#         if i in unicode_unicod_slovnik:
#             list_vstup.append(unicode_unicod_slovnik[i])

#     return list_vstup


# def klice_podle_hodnot(unicod_slovnik, serazeny_vystup):
#     nove_klice = [klic for klic in serazeny_vystup if unicod_slovnik.get(klic) is not None]
#     return nove_klice

# # unicod_slovnik = {"a": 10, "b": 77}
# # serazeny_vystup = [10, 10, 77, 99]

# nove_klice = klice_podle_hodnot(unicod_slovnik, serazeny_vystup)
# print(nove_klice)








# #### Hlavni EXEKUTIVA ################################################################################33


# unicod_slovnik = unicod_slovnik_unicode()
# vystup = (transformace_t_na_u(vstup, unicod_slovnik))
# print(vystup)
# serazeny_vystup = set(vystup)


# # def transformace_t_na_u(vstup, unicode_unicod_slovnik):
# #     # Transformuje text na Unicode

# #     list_vstup = []
# #     for znak in vstup:
# #         if znak in unicode_unicod_slovnik:
# #             list_vstup.append(unicode_unicod_slovnik[znak])

# #     return list_vstup

# # # Zavolání funkce a výpis výsledku
# # vstup = "Hello123"
# # unicode_unicod_slovnik = unicod_slovnik_unicode()
# # vysledek = transformace_t_na_u(vstup, unicode_unicod_slovnik)
# # print(vysledek)
