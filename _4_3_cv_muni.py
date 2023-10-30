
# # du_X_Y.py
# # Nepovinné úkoly
# Cvičení 4.3: Sčítačka
# Úkol:
# Vytvořte program, který bude od uživatele načítat reálná čísla, vždy jedno číslo na
# každém řádku. Když pak uživatel zadá místo čísla znak =, vypíše se součet dosud
# zadaných čísel a program skončí. Součet vypisujte na 2 desetinná místa.
# Vzorový vstup 1:   Vzorový vstup 2:   Vzorový vstup 3:  
# 5 -1.12 =
# 1.2 =
# 0.5
# =
# Vzorový výstup 1:   Vzorový výstup 2:   Vzorový výstup 3: 

    
############################################################3

def naplneni_cisle():
    # Provede plnění čísel do seznamu, ale ještě je nesečte.
    list_cisel = []

    while True:
        vstup = input("Zadejte číslo nebo '=' pro ukončení: ")
        
        if vstup == "=":
            break
        
        try:
            cislo = float(vstup)
            list_cisel.append(cislo)
        except ValueError:
            print("Neplatný vstup, zadejte platné číslo.")
    
    return list_cisel  # Vrátíme seznam čísel po dokončení smyčky

# Zavolání funkce a uložení výsledku do proměnné
seznam_cisel = naplneni_cisle()

# Výpis seznamu čísel
# print("Seznam čísel:", seznam_cisel)

def vlastni_suma_vlozenych_cisel(seznam_cisel: list)-> float:
    suma = 0
    for i in seznam_cisel:
        suma =  suma + i 

    return print(f"Vystup: {suma:.2f}")

vlastni_suma_vlozenych_cisel(seznam_cisel)
