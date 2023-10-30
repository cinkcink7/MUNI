
# du_X_Y.py
# DÚ 5.5: Hledáme kopie
# Úkol:
# Na vstupu získáte několik slov, z nichž jedno se opakuje. Vypište, které slovo to je a
# na kterých dvou pozicích se nachází (pozice počítáme od nuly).
# Hint: Jde to i bez použití funkce index. Stačí využít vhodný typ kolekce.
# Vzorový vstup 1:
# košík bouda kokos olovo mango kokos užovka karate
# Vzorový výstup 1:
# kokos 2 5\
##############################################################################################
# Vysledek :
# retezec = input("Zadej několik slov oddělených mezerou: ")
# slova = retezec.split()
# pozice = {}

# for i, slovo in enumerate(slova):
#     if slovo in pozice:
#         pozice[slovo].append(i)
#     else:
#         pozice[slovo] = [i]

# for slovo, pozice_v_seznamu in pozice.items():
#     if len(pozice_v_seznamu) > 1:
#         pocet_opakovani = len(pozice_v_seznamu)
#         pozice_text = " ".join(map(str, pozice_v_seznamu))
#         print(f"{slovo} {pozice_text}")

###############################################################################################

vstup = input("Zadej několik slov oddělených mezerou, a já zjistím, zda se některá slova opakují: \n")
vstup = vstup.split()

position = {}

for i, slovo in enumerate(vstup):
    if slovo not in position:
        position[slovo] = [i]
    else:
        position[slovo].append(i)

for slovo, pozice in position.items():
    if len(pozice) > 1:
        #print(f"{slovo} se opakuje na pozicích {', '.join(map(str, pozice))}")
        print(f"{slovo} {' '.join(map(str, pozice))}")

##############################################################################################################


# vstup = input("Zadej nekolik slov, oddelene mezerou a ja poznam zdali se nektere opakuje: \n")
# vstup =  vstup.split()
# opakujici_slovo = slovo[]

# pozice = {}


# for i, slovo in enumerate(vstup):

#     # opakujici_slovo = slovo

#     if opakujici_slovo == slovo:

#         pozice[slovo] = i

#         print(slovo, pozice[slovo])

#     else:
#         pass

# vstup = input("Zadej několik slov oddělených mezerou, a já zjistím, zda se některá slova opakují: \n")
# slova = vstup.split()
# pozice = {}

# for i, slovo in enumerate(slova):
#     if slovo in pozice:
#         pozice[slovo].append(i)
#     else:
#         pozice[slovo] = [i]

# for slovo, pozice_v_seznamu in pozice.items():
#     if len(pozice_v_seznamu) > 1:
#         print(f"Slovo '{slovo}' se vyskytuje na pozicích: {', '.join(map(str, pozice_v_seznamu))}")


# retezec = input("Zadej několik slov oddělených mezerou, a já zjistím, zda se některá slova opakují: \n")

# slova = retezec.split()
# pozice = {}

# retezec = input("Zadej několik slov oddělených mezerou, a já zjistím, zda se některá slova opakují: \n")

# slova = retezec.split()
# pozice = {}

# for i, slovo in enumerate(slova):
#     if slovo in pozice:
#         pozice[slovo].append(i)
#     else:
#         pozice[slovo] = [i]

# for slovo, pozice_v_seznamu in pozice.items():
#     if len(pozice_v_seznamu) > 1:
#         pocet_opakovani = len(pozice_v_seznamu)
#         pozice_text = ", ".join(map(str, pozice_v_seznamu))
#         print(f"{slovo}+' '+ {pocet_opakovani}+' '+ {pozice}")

############################################# var b


# #retezec = "košík bouda kokos olovo mango kokos užovka karate slovo"
# retezec = input("Zadej několik slov oddělených mezerou, a já zjistím, zda se některá slova opakují: \n")
# slova = retezec.split()
# pozice = {}

# for i, slovo in enumerate(slova):
#     if slovo in pozice:
#         pozice[slovo].append(i)
#     else:
#         pozice[slovo] = [i]

# for slovo, pozice_v_seznamu in pozice.items():
#     if len(pozice_v_seznamu) > 1:
#         pocet_opakovani = len(pozice_v_seznamu)
#         pozice_text = ", ".join(map(str, pozice_v_seznamu))
#         print(f"Slovo '{slovo}' se vyskytuje {pocet_opakovani}krát na pozicích: {pozice_text}")

###################################################################################################################

# Vysledek :
# retezec = input("Zadej několik slov oddělených mezerou: ")
# slova = retezec.split()
# pozice = {}

# for i, slovo in enumerate(slova):
#     if slovo in pozice:
#         pozice[slovo].append(i)
#     else:
#         pozice[slovo] = [i]

# for slovo, pozice_v_seznamu in pozice.items():
#     if len(pozice_v_seznamu) > 1:
#         pocet_opakovani = len(pozice_v_seznamu)
#         pozice_text = " ".join(map(str, pozice_v_seznamu))
#         print(f"{slovo} {pozice_text}")












