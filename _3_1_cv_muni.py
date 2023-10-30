
# du_X_Y.py
# Nepovinné úkoly
# Cvičení 2.3: Oblíbené číslo
# Alice, Bob a Cyril si chtějí vybrat společné oblíbené číslo.
# • Alici se líbí dvouciferná čísla, která obsahují čtyřku.
# • Bobovi se líbí čísla dělitelná třemi.
# • Cyrilovi se líbi všechna čísla kromě násobků sedmi.
# Úkol:
# Zjistěte, jestli se zadané přirozené číslo n bude líbit všem třem. Výsledek uložte do
# proměnné all_like. (O vstup a výstup se stará předpřipravený kód.)
# Tip: úkol rozdělte na podúkoly a částečné výsledky si ukládejte do pomocných
# proměnných (např. has_2_digits, bob_likes…).
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# 45 42 12
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3:  
# True False False
# 2
# [ ]: n = int(input()) # vstup
# ...
# print(all_like) # výstu
###################################################################################
# import math
# #################################################################################
# # a, b = [float(x) for x in input().split()] # vstup
# vstup = int(input())


# def dvojciferne(vstup: int) -> bool:

#     cislo = list(str(vstup))
#     if len(cislo) == 2:
#         return True
#     else:
#         return False

    
# def delitelnetremi(vstup: int) -> bool:

#     if vstup % 3 == 0:
#         return True
    
#     else: 
#         return False
    
# def nasobkysedmi(vstup: int) -> bool:

#     if vstup % 7 != 0:
#         return True
    
#     else:
#         return False
    
# delitelnetremi = delitelnetremi(vstup)
# print(delitelnetremi)
# nasobkysedmi = nasobkysedmi(vstup)
# print(nasobkysedmi)
# dvojciferne = dvojciferne(vstup)
# print(dvojciferne)

# def main(delitelnetremi, nasobkysedmi, dvojciferne) -> bool:

#     if delitelnetremi == nasobkysedmi == dvojciferne == True:
#         return True
    
#     else:
#         return False

# print(main(delitelnetremi, nasobkysedmi, dvojciferne))

##########################################################################################################

# Procvičení logických výrazů
# Následující úkoly jsou nepovinné, ale užitečné k procvičení logických výrazů. Řešte
# na papír (nebo z hlavy) bez použití Pythonu. Na konci souboru najdete správná řešení.
# 1.
# Máme zadefinované proměnné:
""" x = 2
y = 9
Jaký bude výsledek následujícího výrazu?
x < y and x**3 > y or y % x == 0 or x // y == 0  

false a true 
A) True
B) False
      """
        
# x = 2 
# y = 9
# print(x<y and x**3 > y)  # true  a false ... false
# print(x<y and x**3 > y or y % x == 0) #......false or false ... false
# print(x<y and x**3 > y or y % x == 0 or x// y == 0 )#.................false .... true ... true

""" Jaký bude výsledek následujícího výrazu?
type(x+y) == int and type(x) == type(float(x)) or type(x*y) != type(x/y)
A) True
B) False """
# x = 2
# y = 9
# print(type(x+y))# true and true is true ..... 
# print((type(x)) == type(float(x)))

# print(False or False)

# print(len( "pš\t\t\tt"))
# print( "pš\t\t\tt")
# ##################################################################################################
# A = 'bim bam'
# B = """pštros"""
# C = "pš\t\t\tt"
# D = str(10+10+10)

# delka_A = len(A)
# delka_B = len(B)
# delka_C = len(C)
# delka_D = len(D)

# delky = {'A': delka_A, 'B': delka_B, 'C': delka_C, 'D': delka_D}

# nejdelsi_retezec = max(delky, key=delky.get)
# delka_nejdelsiho = delky[nejdelsi_retezec]

# print(f"Nejdelší řetězec je {nejdelsi_retezec} s délkou {delka_nejdelsiho} znaků.")

###################################################################################################

# print(len('Dobrý den.\n'))
# print(len(''))
# print(len(" "))
# print(len("\t"))

##############################################################################################

# Otázky:
# text = 'Lorem ipsum dolor sit amet'
# Který z těchto výrazů vrátí True?
# (A) text[5] == 'm'
# (B) text[1:4] == 'orem'
# (C) ' ' in text
# (D) text.isalpha()
# Který z těchto výrazů vrátí True?
# (A) text.replace('n', 'f') == text
# (B) text.strip('Lol') == text
# (C) 'abc' + 'def' == 'abc def'
# (D) "5" * 5 == '55555'
# Který z těchto výrazů vrátí True?
# (A) 'Brrrrr no to je zima'.strip('Br').startswith('no')
# (B) 'Brno'.replace('r','rrrrr')[-1] == 'n'
# (C) 'Toto léto stojí za to'.count('to') <= 4
# (D) 'Brno'.find('r') == 'Olomouc'.find('o')

##########################################################################################

# Cvičení 3.1: Je to slovo?
# Úkol:
# Napište kód, který načte řetězec ze standarního vstupu pomocí funkce input. Poté
# rozhodne, jestli načtený řetězec je jedno slovo (tj. skládá se pouze z písmen). Pokud
# ano, vypíše True, v opačném případě False. Pro výpis použijte funkci print.
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# Alohomora Wingardium leviosa 9
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3:  
# True False False
# [ ]: ...
# # Vzorové vstupy pro kopírování:
# # Alohomora
# # Wingardium leviosa
# 9

# vstup = input("Vstup :\n")
# vstup = vstup.split()
# #delka_vstupu = len(vstup)


# def zdali_je_to_vice_str(vstup: str) -> bool:
#     if delka_vstupu >= 2:
#         return True
#     else:
#         return False

# print(zdali_je_to_vice_str(vstup))

###################################################################################################

# VCvičení 3.2: Násobička
# Úkol:
# Napište kód, který ze standarního vstupu načte dvě celá čísla a na výstup vypíše jejich
# součin.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 2 3 -111 -6
# Vzorový výstup 1:   Vzorový výstup 2: 


# vstup = input()
# vstup = vstup.split()

# def prevod_ze_str_na_int(vstup: str) -> int:

#     list_cisel = []
#     for i in vstup:
#         cislo = int(i)
#         list_cisel.append(cislo)
#     soucin = 1
#     for j in list_cisel:
#         soucin = soucin * j

#     return soucin

# print(prevod_ze_str_na_int(vstup))

#######################################################################################################33

# Cvičení 3.3: Palindrom?
# Palindrom je slovo nebo věta, která má stejné pořadí písmen zleva doprava a zprava
# doleva. Nezáleží při tom na velikosti písmen a na výskytu mezer.
# Úkol:
# Ze vstupu načtěte řetězec a rozhodněte, zda je to palindrom. (Můžete spoléhat, že
# vstup nebude obsahovat jiné znaky kromě písmen a mezer.)
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# Jelenovi pivo nelej Jelen chce pivo Anna
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3:  



vstup = input("Vstup: \n")
retezec = vstup.replace(" ", '')
maly_retezec = retezec.lower()
maly_retezec_pozpatku = maly_retezec[::-1]
print(maly_retezec_pozpatku)

def palindrom(vstup: str) -> bool:
    pocet_opakovani = len(maly_retezec)  # Initialize pocet_opakovani
    for i in range(pocet_opakovani):
        if maly_retezec[i] != maly_retezec_pozpatku[i]:
            return False

    return True

is_palindrome = palindrom(vstup)



print(is_palindrome)
print(maly_retezec)




###################################################################################################

# def je_palindrom(retezec):
#     retezec = retezec.lower().replace(" ", "")  # Převeď na malá písmena a odstraň mezery
#     retezec_pozpatku = retezec[::-1]  # Vytvořte řetězec pozpátku
#     return retezec == retezec_pozpatku  # Porovnej řetězec s jeho verzí pozpátku

# vstup = input("Vstup: ")
# if je_palindrom(vstup):
#     print("Zadáno slovo nebo věta je palindrom.")
# else:
#     print("Zadáno slovo nebo věta není palindrom.")
