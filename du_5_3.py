
# du_X_Y.py

# DÚ 5.3: Nákupy
# Úkol:
# Napište kód, který ze vstupu načte dva řádky:
# • ceník zboží (oddělený čárkami a dvojtečkami bez mezer)
# • obsah nákupního košíku (oddělený čárkami bez mezer)
# Ceník načtěte a uložte do vhodné kolekce. Poté spočítejte celkovou hodnotu zboží v
# nákupním košíku a vypište ji na výstup v požadovaném formátu.
# Vzorový vstup 1:
# Rohlík:2.20,Banán:5.00,Jogurt:8.90,Sušenky:27.50,Čokoláda:24.00,Mléko:17.90,Spaghetti:21.90
# Rohlík,Rohlík,Rohlík,Mléko,Čokoláda
# Vzorový výstup 1:
# Celková cena: 48.50 Kč


cenik = {"Rohlík": 2.20," Banán": 5.00, "Jogurt": 8.90, "Sušenky": 27.50, "Čokoláda": 24.00, "Mléko":17.90, "Spaghetti":21.90}

nakup = input("Zadej nakupni seznam: \n")
nakup = nakup.split()

celkova_cena = 0

for klic in nakup:

    cena_polozky = cenik[klic]
    celkova_cena =  celkova_cena + cena_polozky

print(f"Celkova cena: {celkova_cena:.2f}")






