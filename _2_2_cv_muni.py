
# du_X_Y.py
# Nepovinné úkoly
# Cvičení 2.2: Pravoúhlý trojúhelník
# Mějme pravoúhlý trojúhelník 𝐴𝐵𝐶 s odvěsnami 𝑎, 𝑏 a přeponou 𝑐. Pro úhel 𝛼 platí tyto
# vztahy:
# sin 𝛼 =
# 𝑎
# 𝑐
# cos 𝛼 =
# 𝑏
# 𝑐
# tan 𝛼 =
# 𝑎
# 𝑏
# Úkol:
# Ze zadaných délek odvěsen a, b spočítejte velikost úhlu 𝛼 ve stupních. Výsledek uložte
# do proměnné alpha. (O vstup a výstup se stará předpřipravený kód.)
# Vzorový vstup:
# 10 20
# Vzorový výstup:
# 26.565
# [ ]: a, b = [float(x) for x in input().split()] # vstup
# ...
# print(f'{alpha:.3f}') # výstup (na 3 desetinná místa

###################################################################################
import math
#################################################################################

# vstup = input()
# vstup = vstup.split() # ted to mam list o dvou polozkach str
# # a, b = [float(x) for x in input().split()] # vstup

# def prevest_na_float(vstup: str) -> list[float]:

#     vstup_floats = []
#     for item in vstup:

#         item = float(item)
#         vstup_floats.append((item))

#     return vstup_floats

# vstup_list_float = prevest_na_float(vstup)

# # sin(alfa) = a/c
# # cos(alfa) = b/c
# # tan(afla) = a/b

# uhel_v_radianech = vstup_list_float[0]/vstup_list_float[1]
# # print(f"sin: {uhel_v_radianech}")
# uhel_ve_stupnich = math.degrees(uhel_v_radianech)
# print(f'{uhel_ve_stupnich:.3f}') # výstup (na 3 desetinná místa


###########################################################################33
# varB

a, b = [float(x) for x in input().split()] # vstup
print(a)
print(b)
print(a, b)
# sin(alfa) = a/c
# cos(alfa) = b/c
# tan(afla) = a/b

uhel_v_radianech = a/b
# print(f"sin: {uhel_v_radianech}")
uhel_ve_stupnich = math.degrees(uhel_v_radianech)
print(f'{uhel_ve_stupnich:.3f}') # výstup (na 3 desetinná místa      
        





