
# du_X_Y.py
# DÚ 4.2: Kalkulačka
# Úkol:
# Na vstupu získate dvě desetinná čísla oddělená matematickým operátorem (před a za
# operátorem bude vždycky mezera). Proveďte výpočet a vypište výsledek zaokrouhlený
# na 2 desetinná místa.
# Možné operace:
# • sčítání +
# • odečítání -
# • násobení *
# • dělení /
# Pokud bude zadaný jiný operátor, vypište na výstup ERROR.
# Vzorový vstup:
# 1 + 2.5
# Vzorový výstup:
# 3.50
# Vyzkoušejte také:
# 3 - 4
# 5 * 6
# 7 / 8
# 9 & 10

# cisla = input("Zadej dve čísla oddělená mezerami: ").split()

# cislo_1 = float(cisla[0])
# operator = str(cisla[1])
# cislo_2 = float(cisla[2])

# # print(cislo_1)
# # print(cislo_2)
# # print(operator)

# if operator == "+":
#     vysledek = float(cislo_1) + float(cislo_2)
#     print(f"{round(vysledek, 2)}")
   
# elif operator == "/":
#     vysledek = float(cislo_1) / float(cislo_2)
#     print(f"{round(vysledek, 2)}")

# elif operator == "*":
#     vysledek = float(cislo_1) * float(cislo_2)
#     print(f"{round(vysledek, 2)}")


# elif operator == "-":
#     vysledek = float(cislo_1) - float(cislo_2)
#     print(f"{round(vysledek, 2)}")


# # if operator == "&":
# #     vysledek = float(cislo_1) & float(cislo_2)
# #     print(f"{round(vysledek, 2)}")

# else:

#     print("ERROR")


#################################################################################################################


# Načtěte vstupní řetězec
input_string = input("Zadejte dvě desetinná čísla oddělená operátorem (+, -, *, /): ")

# Rozdělte vstupní řetězec na číslo a operátor
parts = input_string.split()
if len(parts) != 3:
    print("ERROR")
else:
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    # Provádění matematických operací
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("ERROR (dělení nulou)")
        else:
            result = num1 / num2
    else:
        print("ERROR (neznámý operátor)")

    # Výstup výsledku
    if 'result' in locals():
        print("{:.2f}".format(result))



