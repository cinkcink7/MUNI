
# du_X_Y.py
# DÚ 4.3: Záplava čísel
# Úkol:
# Ze vstupu načtěte řetězec obsahující pouze číslice. Vypište na výstup řetězec, který
# bude obsahovat každou číslici ze vstupu tolik krát, kolik je hodnota číslice (tj. dvě
# 2
# dvojky, pět pětek…).
# Vzorový vstup 1:
# 25104
# Vzorový výstup 1:
# 225555514444

# retezec = (input("Napis cilo: \n"))

# novy_retezec = ""

# for znak in retezec:
#     if znak == '2':
#         novy_retezec += '2' * 2
#     elif znak == '3':
#         novy_retezec += '3' * 3
#     elif znak == '4':
#         novy_retezec += '4' * 4
#     elif znak == '5':
#         novy_retezec += '5' * 5
#     elif znak == '6':
#         novy_retezec += '6' * 6
#     elif znak == '7':
#         novy_retezec += '7' * 7
#     elif znak == '8':
#         novy_retezec += '8' * 8
#     elif znak == '9':
#         novy_retezec += '9' * 9
#     elif znak == '0':
#         novy_retezec += '0' * 0
#     else:
#         novy_retezec += znak

# print(novy_retezec)


###########################################################################################

#var b

# Načtěte vstupní řetězec
input_str = input("Zadejte řetězec obsahující číslice: ")

# Inicializace výstupního řetězce
output_str = ""

# Projděte vstupní řetězec
for char in input_str:
    if char.isdigit():
        # Převeďte znak na číslo a zopakujte ho tolikrát, kolik je jeho hodnota
        output_str += char * int(char)

# Výstup výsledku
print(output_str)






