
# # du_X_Y.py
# Cvičení 5.5: Pozice maxima
# Na vstupu získate posloupnost celých čísel oddělených mezerou. Vaším úkolem je
# nalézt největší číslo a vypsat jeho pozici a hodnotu. Pokud bude více největších čísel,
# vypište pozici prvního. Při výpisu počítejte pozice od jedničky (ne od nuly).
# Vzorový vstup 1:   Vzorový vstup 2:  
# 150 13 7 10 11 2 3 5 5 1 5
# Vzorový výstup 1:   Vzorový

vstup = input("Vstup: \n")
vstup = vstup.split()
vstup = [int(x) for x in vstup]
Max = max(vstup)

def pozice_maxima():

    for i, value in enumerate(vstup):
        if Max == value:

            pozice = i + 1 

    return (pozice)

print(pozice_maxima())

##############################################################################
# for index, hodnota in enumerate(my_list):
#     print(f"Na pozici {index} je {hodnota}")

###########################################################################
#### toto je basic situace pro vstup = [int(x) for x in vstup]
# def prevod_str_na_int():
#     vstup1 = []
#     for i in vstup:
#         cislo = int(i)
#         vstup1.append(cislo)

#     return vstup1

# vstup = prevod_str_na_int()
# print(vstup)

####################################################################