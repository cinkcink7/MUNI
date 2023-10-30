
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

# DÚ 6.5: Výpis slovníku
# Úkol:
# Napište funkci print_dict, která bere slovník (parametr dictionary) a ten hezky
# vypíše na výstup v tomto formátu (viz vzorový výstup):
# • řádek s nadpisem (parametr title) a počtem klíčů ve slovníku
# • řádky s jednotlivými dvojicemi klíč:hodnota, seřazené podle klíčů, odsazené o 4
# mezery
# Dále UPRAVTE HLAVIČKU funkce tak, aby ji bylo možné volat i bez parametru title
# (v takovém případě se místo nadpisu vypíše pouze dict).
# Funkce nemá nic vracet, pouze vypisovat (tj. návratová hodnota je None). Klíče a
# hodnoty mohou být libovolného typu, při jejich výpisu stačí použít defaultní formát.
# Vzorové volání 1:
# print_dict({'bob': 10, 'cyril': 6, 'alice': 9}, title='Skóre v
# Kloboučku Hop')
# Vzorový výstup 1:
# Skóre v Kloboučku Hop [3]:
# alice: 9
# bob: 10
# cyril: 6
# Vzorové volání 2:
# print_dict({1: 1, 3: 9, 5: 25, 2: 4, 4: 16})
# Vzorový výstup 2:
# dict [5]:
# 1: 1
# 2: 4
# 3: 9
# 4: 16
# 5: 25
# [ ]: def print_dict(dictionary: dict, title: str) -> None:
# ...
# # print_dict({'bob': 10, 'cyril': 6, 'alice': 9}, title='Skóre v␣
# ↪Kloboučku Hop')
# # print_dict({1: 1, 3: 9, 5: 25, 2: 4, 4: 16}


#varA

# def print_dict(dictionary: dict, title: str = "dict") -> None:
#     # Výpis nadpisu a počtu klíčů
#     print(f"{title} [{len(dictionary)}]:")

#     # Seřazení klíčů slovníku
#     sorted_keys = sorted(dictionary.keys())

#     # Výpis dvojic klíč:hodnota
#     for key in sorted_keys:
#         value = dictionary[key]
#         print(f"    {key}: {value}")

# # Příklady použití
# print_dict({'bob': 10, 'cyril': 6, 'alice': 9}, title='Skóre v Kloboučku Hop')
# print_dict({1: 1, 3: 9, 5: 25, 2: 4, 4: 16})


###################################################################################

#varB

# def print_dict(dictionary, title):
#     sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[0]))
    
#     print(f"{title} [{len(sorted_dict)}]:")
    
#     for key, value in sorted_dict.items():
#         print(f"    {key}: {value}")

# print_dict({'bob': 10, 'cyril': 6, 'alice': 9}, title='Skóre v Kloboučku Hop')

########################################################################################

#varC

# def print_dict(dictionary: dict, title: str) -> None:

#     pocet_klicu_ve_slovniku = len(dictionary)
#     print(f"{title}  [{pocet_klicu_ve_slovniku}]")

#     serazeny_slovnik_dle_klice = sorted(dictionary.items())
                                        

#     for key, value in serazeny_slovnik_dle_klice:

#         print(f"    {key}: {value}")


      

# print_dict({'bob': 10, 'cyril': 6, 'alice': 9}, title='Skóre v Kloboučku Hop')
# print_dict({1: 1, 3: 9, 5: 25, 2: 4, 4: 16})

# # Skóre v Kloboučku Hop [3]:
# # alice: 9
# # bob: 10
# # cyril: 6

#####################################################################################
# varD

def print_dict(dictionary: dict, title: str = "dict") -> None:
    # Výpis nadpisu a počtu klíčů
    print(f"{title} [{len(dictionary)}]:")

    # Seřazení klíčů slovníku
    sorted_keys = sorted(dictionary.keys())

    # Výpis dvojic klíč:hodnota
    for key in sorted_keys:
        value = dictionary[key]
        print(f"    {key}: {value}")

# Příklady použití
print_dict({'bob': 10, 'cyril': 6, 'alice': 9}, title='Skóre v Kloboučku Hop')
print_dict({1: 1, 3: 9, 5: 25, 2: 4, 4: 16})


##########################################################################################












