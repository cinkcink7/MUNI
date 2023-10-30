
# du_X_Y.py

# Povinné domácí úkoly
# DÚ 3.1: Vědecký formát
# Úkol:
# Napište kód, který se standardního vstupu načte číslo a vypíše ho na výstup ve
# vědeckém formátu se dvěma desetinnými místy.
# Vzorový vstup:
# 40800000000.00000000000000
# Vzorový výstup:
# 4.08E+10

cislo = float(input("Napis cislo: \n"))
vedecky_format = "{:.2E}".format(cislo)
print(vedecky_format)

