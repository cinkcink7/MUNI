
# du_X_Y.py

# Ú 4.1: Začíná, končí nebo obsahuje?
# Úkol:
# Na vstupu získáte dva řetezce oddělené mezerou. Otestujte jestli první řetězec začíná,
# končí nebo aspoň obsahuje druhý řetězec. Možné výstupy:
# • '…' starts and ends with '…'
# • '…' starts with '…'
# • '…' ends with '…'mo6n0
# • '…' contains '…'
# • '…' does not contain '…'
# (Místo … doplňte první a druhý řetězec.)
# Vzorový vstup:
# alobal al
# Vzorový výstup:
# 'alobal' starts and ends with 'al'
# Vyzkoušejte také tyto vstupy:
# bussiness bus
# autobus bus
# alobal oba
# alobal bus

# retezec = input("Zadej dve reteyzce oddělená mezerami: ").split()

# if len(retezec) != 2:
#     print("Zadal jsi jeden retezec.")

# elif len(retezec) >= 2:
#     r = str(retezec[0])
#     #print(r)
#     v = str(retezec[1])
#     #print(v)

#     zacatek_r = r[0]
#     #print(zacatek_r)
#     konec_r = r[len(r)-1]
#     #print(konec_r)

#     zacatek_v = v[0]
#     #print(zacatek_v)
#     konec_v = r[len(v)-1]
#     #print(konec_v)

#     if zacatek_r == zacatek_v and konec_r == konec_v:
#         print(f" {r} + start with {zacatek_r} end with {konec_r}")

#########################################################################################################################

# # Načtení dvou řetězců oddělených mezerou
# input_str = input("Zadejte dva řetězce oddělené mezerou: ")
# first_str, second_str = input_str.split()

# # Test, zda první řetězec začíná druhým řetězcem
# if first_str.startswith(second_str):
#     start_result = f"'{first_str}' starts with '{second_str}'"
# else:
#     start_result = f"'{first_str}' does not start with '{second_str}'"

# # Test, zda první řetězec končí druhým řetězcem
# if first_str.endswith(second_str):
#     end_result = f"'{first_str}' ends with '{second_str}'"
# else:
#     end_result = f"'{first_str}' does not end with '{second_str}'"

# # Test, zda první řetězec obsahuje druhý řetězec
# if second_str in first_str:
#     contains_result = f"'{first_str}' contains '{second_str}'"
# else:
#     contains_result = f"'{first_str}' does not contain '{second_str}'"

# # Výstup
# print(start_result)
# print(end_result)
# print(contains_result)


########################################################################################
# Načtení vstupního řetězce odděleného mezerou
input_string = input("Zadejte dva řetězce oddělené mezerou: ")
strings = input_string.split()

# Inicializace proměnných pro výsledné zprávy
result = ""

# Zkontrolovat, zda první řetězec začíná druhým řetězcem
if strings[0].startswith(strings[1]):
    result += f"'{strings[0]}' starts with '{strings[1]}'"

# Zkontrolovat, zda první řetězec končí druhým řetězcem
if strings[0].endswith(strings[1]):
    if result:
        result += ", "
    result += f"'{strings[0]}' ends with '{strings[1]}'"

# Zkontrolovat, zda první řetězec obsahuje druhý řetězec
if strings[1] in strings[0]:
    if result:
        result += ", "
    result += f"'{strings[0]}' contains '{strings[1]}'"

# Zkontrolovat, zda první řetězec je stejný jako druhý řetězec
if strings[0] == strings[1]:
    if result:
        result += ", "
    result += f"'{strings[0]}' is equal to '{strings[1]}'"

# Pokud neplatí žádná z výše uvedených možností
if not result:
    result = f"'{strings[0]}' does not contain or is not equal to '{strings[1]}'"

# Výstup
print(result)