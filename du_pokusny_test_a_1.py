
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat neakou funkci.
#  Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).


# Vzorový vstup:
# red green purple green green purple red purple red green red green
# Vzorový výstup:
# Sample size: 12
# Distinct values: 3 (green, purple, red)
# Shortest: red
# Longest: purple
# Graph:
# green : 42% #####
# red : 33% ####
# purple: 25% ###

# Načtěte řádek s hodnotami ze vstupu a převeďte na seznam řetězců (2
# from math import ceil
# ##########################################


# vstup = input()
# vstup = vstup.split()
# novy_text = ''.join(vstup)
# print(novy_text)

# ####

# # Vypište rozsah souboru (počet prvků) (1

# print((f"Sample size: {len(vstup)}"))

# #Vypište počet různých hodnot a výčet těchto hodnot (abecedně) (4)

# print(vstup)
# #######################################################################
# ####      VYPOCTY NA POCET BAREV       ####


# def pocet_kazde_green(vstup):
#     sumagreen = 0
#     for barva in vstup:
#         if barva == "green":
#             sumagreen = sumagreen + 1
#     return sumagreen

# def pocet_kazde_red(vstup):
#     sumared = 0
#     for barva in vstup:
#         if barva == "red":
#             sumared = sumared + 1
#     return sumared

# def pocet_kazde_purple(vstup):
#     sumapurple = 0
#     for barva in vstup:
#         if barva == "purple":
#             sumapurple = sumapurple + 1
#     return sumapurple

# def cetnostRed(sumared):

#     redRelativni = sumared / sumabarev * 100
#     zaokrouhleneRedRelativni = ceil(redRelativni)
#     graf = "#"*zaokrouhleneRedRelativni
#     stavBarvaRed = (f"{zaokrouhleneRedRelativni} % {graf}")
#     return stavBarvaRed
    
# def cetnostGreen(sumagreen):

#     GreenRelativni = sumagreen / sumabarev * 100
#     zaokrouhleneGreenRelativni = ceil(GreenRelativni)
#     graf = "#"*zaokrouhleneGreenRelativni
#     stavBarvaGreen = (f"{zaokrouhleneGreenRelativni} % {graf}")
#     return stavBarvaGreen 

# def cetnostPurple(sumapurple):

#     PurpleRelativni = sumapurple / sumabarev * 100
#     zaokrouhlenePurpleRelativni = ceil(PurpleRelativni)
#     graf = "#"*zaokrouhlenePurpleRelativni
#     stavBarvaPruple= (f"{zaokrouhlenePurpleRelativni} % {graf}")
#     return stavBarvaPruple 

# # cetnostBarvy = []

# # def volneLozeneList():
# #     cetnostBarvy = []
# #     volneLozeneList = volneLozeneList.append(cetnostBarvy)




# # def serazeni_od_nejvetsi(sumagreen, sumared, sumapurple):
# #     #seradi bravy dle cetnosti
   
# #     for i in range(len)
# #         serazeni = serazeni.append() 
   

# #     pass



# sumagreen = pocet_kazde_green(vstup)
# #print(sumagreeen)
# sumared = pocet_kazde_red(vstup)
# #print(sumared)
# sumapurple = pocet_kazde_purple(vstup)
# #print(sumapurple)
# sumabarev = sumared + sumapurple + sumagreen

# print(sumabarev)
# print(cetnostRed(sumared))
# print(cetnostGreen(sumagreen))
# print(cetnostPurple(sumapurple))

# # Vypočet cetnosti
# cetnosti = [
#     (cetnostRed(sumared, sumabarev), "Red"),
#     (cetnostGreen(sumagreen, sumabarev), "Green"),
#     (cetnostPurple(sumapurple, sumabarev), "Purple")
# ]

# # Seřazení podle cetnosti (od největšího po nejmenší)
# serazeno = sorted(cetnosti, reverse=True)

# # Tisk výsledků
# for cetnost, barva in serazeno:
#     print(cetnost)
#     print(barva)



### var b

from math import ceil

def pocet_kazde_barvy(vstup, barva):
    pocet = 0
    for b in vstup:
        if b == barva:
            pocet += 1
    return pocet

def cetnost_barvy(pocet, celkem_barev, barva):
    if celkem_barev == 0:
        relativni = 0
    else:
        relativni = pocet / celkem_barev * 100
    zaokrouhleno = ceil(relativni)
    graf = "#" * zaokrouhleno
    stav = f"{zaokrouhleno} %  {barva}"
    return stav

vstup = input()
vstup = vstup.split()
sumabarev = len(vstup)

barvy = ["Red", "Green", "Purple"]
cetnosti = []

for barva in barvy:
    pocet = pocet_kazde_barvy(vstup, barva)
    cetnost = cetnost_barvy(pocet, sumabarev, barva)
    cetnosti.append((cetnost, barva))

# Seřazení podle cetnosti (od největšího po nejmenší)
serazeno = sorted(cetnosti, reverse=True)

# Tisk výsledků
for cetnost, barva in serazeno:
    print(cetnost)

