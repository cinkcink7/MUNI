
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat neakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).
# Úkol 3 (10 bodů)
# V tomto úkolu budeme řešit dvojsměrku – jednodušší verzi osmisměrky. Zadání dvojsměrky sestává z dlouhého řetězce písmen
#  a seznamu hledaných slov. Tato slova
# potřebujeme najít v řetězci a škrtnout je. Slova mohou být v řetězci zapsána zleva
# doprava nebo zprava doleva. Tajenku pak získáme spojením zbylých neškrtnutých
# písmen.
# Doplňte funkci solve_puzzle, která bere dva argumenty – řetězec písmen a seznam
# hledaných slov. Návratovou hodnotou funkce bude vyluštěná tajenka.
# Příklad dvojsměrky:
# ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM
# Hledaná slova: FUNKCE MOST MYŠ STROM VÝLET ŠTVANEC
# Řešení:
# Po vyškrtnutí všech hledaných slov jsme našli tajenku: ZIMA.
# Vzorové volání:
# solve_puzzle('ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM', ['FUNKCE', 'MOST', 'MYŠ', 'STROM', 'VÝLET', 'ŠTVANEC'])
# Vzorový výsledek:
# 'ZIMA'
# [ ]: from __future__ import annotations
# def solve_puzzle(text: str, words: list[str]) -> str:
# 3
# ...
# # solve_puzzle('ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM', ['FUNKCE', 'MOST',␣
# ↪'MYŠ', 'STROM', 'VÝLET', 'ŠTVANEC']) # 'ZIMA'
# # solve_puzzle('AZÁVSVBANÁNAPOKRMAKOŽÍŠEKARAMŘLIBOMÁZUBYK', ['BANÁN',␣
# ↪'KOPANÁ', 'KOŽÍŠEK', 'MARAKEŠ', 'MOBIL', 'POKRM', 'VÁZA', 'ZUBY'])␣
# ↪ # 'SVAŘÁK'
# # solve_puzzle('ŽALHICHLAPATITCPESPEKSUKRUMORRSOLONOHTYPVČIBALGINÍ',␣
# ↪['APATIT', 'BIČ', 'CHLAP', 'CIHLA', 'IBALGIN', 'LOS', 'MOR',␣
# ↪'PES', 'PYTHON', 'RUM', 'SKEPSE', 'ŽAL']) # 'CUKROVÍ


words = "'FUNKCE', 'MOST', 'MYŠ', 'STROM', 'VÝLET', 'ŠTVANEC'"
text =  "ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM"
text_pozpatku = text[::-1]



# def zjisti_pismena(words, text):
    

#     words = words.split(', ')
#     zjistena_pismena = []

#     for i in words:
#         if i in text:
#             a = i
#             zjistena_pismena.append(a)

#     return(zjistena_pismena)
    

# print(zjisti_pismena(words, text))

# words = "FUNKCE MOST MYŠ STROM VÝLET ŠTVANEC"
# text =  "ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM"
# text_pozpatku = text[::-1]

# words = words.split(' ')
# zjistena_pismena = []
# print(words)

# for i in words:
#     if i in text:
#         a = i
#         zjistena_pismena.append(a)

# print(zjistena_pismena)


# words = "'FUNKCE', 'MOST', 'MYŠ', 'STROM', 'VÝLET', 'ŠTVANEC'"
# text =  "ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM"
# text_pozpatku = text[::-1]

# words = words.replace("'", "") # Odstraníme jednoduché uvozovky kolem slov
# words = words.split(', ') # Rozdělíme slova do seznamu na základě čárky a mezer
# zjistena_pismena = []

# # for i in words:
# #     if i in text:
# #         a = i
# #         zjistena_pismena.append(a)

# # print(zjistena_pismena)

# def kontrola_obsahu_slov(words, text):
#     zjistena_pismena = []
#     for i in words:
#         if i in text:
#             a = i
#             zjistena_pismena.append(a)

#     return zjistena_pismena

# zjistena_pismena_popredu = kontrola_obsahu_slov(words, text)
# zjistena_pismena_pozadu= kontrola_obsahu_slov(words, text_pozpatku)      
# # print(zjistena_pismena_popredu)
# # print(zjistena_pismena_pozadu)


# def prevod_listu_na_str(list):

#     # list = ['FUNKCE', 'MOST', 'STROM', 'VÝLET']
#     prevedeny_list_na_str = ', '.join(list)
#     return prevedeny_list_na_str
    
    
# prevod_listu_na_str_popredu = prevod_listu_na_str(zjistena_pismena_popredu)
# prevod_listu_na_str_pozadu = prevod_listu_na_str(zjistena_pismena_pozadu)

# print(prevod_listu_na_str_popredu)
# print(prevod_listu_na_str_pozadu)

# # zbyla_pismena_popredu = text - prevod_listu_na_str_popredu


# prevod_listu_na_str_popredu_na_jeden_str = prevod_listu_na_str_popredu.replace(", ", "") # Odstraní čárky a mezery
# jeden_text_popredu = "".join(prevod_listu_na_str_popredu_na_jeden_str.split())
# # print(jeden_text_popredu)
# prevod_listu_na_str_pozadu_na_jeden_str = prevod_listu_na_str_pozadu.replace(", ", "") # Odstraní čárky a mezery
# jeden_text_pozadu = "".join(prevod_listu_na_str_pozadu_na_jeden_str.split())
# # print(jeden_text_pozadu)

# for i in jeden_text_popredu:

#     # rozepisu char z jeden_text_popredu/pozadu a porovnam na textu
#     zbyla_pismena_popredu =''
#     if i in text:

#         zbyla_pismena_popredu = zbyla_pismena_popredu + i

#     print(f"{zbyla_pismena_popredu}...........")


    #######################################################################

    # varB

def solve_puzzle(text: str, words: list[str]) -> str:
    tajenka = list(text)  # Převedeme řetězec na seznam znaků

    for slovo in words:
        if slovo in ''.join(tajenka):
            for i in range(len(tajenka) - len(slovo) + 1):
                if ''.join(tajenka[i:i + len(slovo)]) == slovo:
                    for j in range(len(slovo)):
                        tajenka[i + j] = ' '

    return ''.join(znak for znak in tajenka if znak != ' ')

# Příklad použití
text = 'ZFUNKCENAVTŠIMOSTROMMVÝLETAŠYM'
slova = ['FUNKCE', 'MOST', 'MYŠ', 'STROM', 'VÝLET', 'ŠTVANEC']
tajenka = solve_puzzle(text, slova)
print(tajenka)  # Výstup: 'ZIMA'
