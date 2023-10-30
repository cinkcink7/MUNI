
# du_X_Y.py
# Nepovinné úkoly


# Cvičení 3.4: Zvýrazňovač
# Úkol:
# Na vstupu bude zadáno jedno slovo, mezera, a pak celá věta. Vypište tuto větu na
# výstup, s tím, že každý výskyt zadaného slova bude vypsán velkými písmeny.
# Vzorový vstup 1:   Vzorový vstup 2:  
# oko Mám oko špinavé od čokolády. jelen Pivo jelenům nenaléváme!
# Vzorový výstup 1:   Vzorový výstup 2:  
# Mám OKO špinavé od čOKOlády. Pivo JELENům nenaléváme!
# [ ]: ...
# # Vzorové vstupy pro kopírování:
# # oko Mám oko špinavé od čokolády.
# # jelen Pivo jelenům nenaléváme!

# # oko Mám oko špinavé od čokolády.
vstup = input("Vstup: \n")
vstup = vstup.split()
slovo = vstup[0]
velke_slovo = slovo.upper()
veta = vstup[1:] 
veta = " ".join(vstup[1:]) 

if slovo in veta:

    vystup = veta.replace("oko", "OKO")

print(vystup)