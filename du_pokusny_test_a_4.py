
# du_X_Y.py
# V úkolech v této sadě je potřeba (narozdíl od předchozích sad) vždy zadefinovat neakou funkci. Není třeba načítat vstup pomocí funkce input, testy budou volat Vaši
# funkci tak, jak uvádí vzorové volání.
# Pokud je uvedené vzorové volání a vzorový výsledek, chce se od Vás, aby návratovou
# hodnotou vzorového volání byl vzorový výsledek (return).
# Pokud je uvedené vzorové volání a vzorový výstup, nemá funkce vracet žádnou
# návratovou hodnotou, ale má vypisovat vzorový výstup (print).

# Úkol 4 (8 bodů)
# Napište program, který načte ze vstupu jeden řádek složený z reálných čísel, oddělených libovolným počtem mezer. 
# Z těchto čísel pak vybere pouze čísla v intervalu 0
# až 10 (včetně), spočítá jejich součet, a tento součet vypíše na výstup jako reálné číslo
# se dvěma desetinnými místy. Počet čísel není omezený (může být i nula čísel, pak je
# součet nula).
# Vzorový vstup:
# 3.14 11 -3.5 9
# Vzorový výstup:
# 12.14


vstup = "13 5.5 888 999   7.8 0.1   11"
vstup = "0"
vstup = "13 5.5 888 999   7.8 0.1  10  11"
vstup = "13 5.5 888 999   7.8 0.1  10  -55 -88 999 -11"

vstup = vstup.split(" ")
print(vstup)
vstup_1 = []
for i in vstup:

    if i !='':
        vstup_1.append(i)
print(vstup_1)

vstup_2 = []
for i in vstup_1:

    a = float(i)
    vstup_2.append(a)

print(vstup_2)


vystup = []
for i in vstup_2:

    if 0<i<=10:

        vystup.append(i)

print(vystup)

suma = 0
for i in vystup:

    suma = suma + i

print(f"{suma:.2f}")














