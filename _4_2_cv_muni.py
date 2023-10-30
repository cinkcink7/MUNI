
# # du_X_Y.py
# # Nepovinné úkoly

# Testování čísel
# Úkol:
# Ze vstupu načtěte celé číslo.
# 1. Otestujte, jestli jsme dostali číslo z intervalu 0–100 (včetně)
# 2. Pokud ano, otestujte, jestli je číslo dělitelné pěti, třemi nebo oběma čísly zároveň
# Na výstup vypište nejvhodnější z těchto hlášek:
# • Out of range (pokud je mimo intervalu 0 až 100)
# • Divisible by 3 and 5
# • Divisible only by 3
# • Divisible only by 5
# • Not divisible by 3 or 5
# Vzorový vstup 1:   Vzorový vstup 2:  
# 100 101
# Vzorový výstup 1:   Vzorový výstup 2:

vstup = int(input("Napis te cele cislo od 0-100: \n"))

def rozsah_cisla(vstup: int) -> bool:
    #kontroluje zdali je cislo od 0-100 vcetne

    if vstup >= 0 and vstup <= 100:
        return True
    else:
        return False
    
def delitelnost_peti(vstup):
    #kontroluje delitelnost vstupu peti

    if vstup % 5 == 0:
        return True
    else:
        return False
    
def delitelnost_tremi(vstup):
    #kontroluje delitelnost vstupu tremi

    if vstup % 3 == 0:
        return True
    else:
        return False
    
def delitelnost_jakTremi_takPeti(vstup):
    
    if vstup % 3 == 0 and vstup % 5 == 0:
        return True
    else:
        return False
########################################################################   
####### hlavni program  #####

def hlavni_program(vstup):
    #hlavni exekuce 

    kontrola = rozsah_cisla(vstup)
    if kontrola != True:
        print ("Vase cislo neni v rozsahu 0-100")
        exit()

    else: 

        if delitelnost_jakTremi_takPeti(vstup):

            return (print(f"je delitelne peti a tremi {vstup}"))

        elif delitelnost_peti(vstup) == True:

            return (print(f"je delitelne peti {vstup}"))

        elif delitelnost_tremi(vstup) == True:

            return (print(f"je delitelne tremi {vstup}"))
        

hlavni_program(vstup)


    


