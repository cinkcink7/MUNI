
# # du_X_Y.py
# # Nepovinné úkoly

# vičení 4.1: Kvadratická rovnice
# V této ukázce si napíšeme program pro řešení kvadratické rovnice. Obecně máme
# kvadratickou rovnici definovanou takto:
# 𝑎𝑥2 + 𝑏𝑥 + 𝑐 = 0
# Kvadratická rovnice může mít v oboru reálných čísel dva, jeden nebo žádné kořeny.
# Počet kořenů můžeme určit podle hodnoty diskriminantu 𝐷:
# 𝐷 = 𝑏2 − 4𝑎𝑐
# Pokud je 𝐷 kladné, rovnice má dva kořeny 𝑥1
# , 𝑥2
# . Ty spočítáme podle vzorců:
# 𝑥1 =
# −𝑏 − √
# 𝐷
# 2𝑎
#  𝑥2 =
# −𝑏 + √
# 𝐷
# 2𝑎
# Když je 𝐷 rovno nule, rovnice má pouze jeden kořen 𝑥, který je:
# 𝑥 =
# −𝑏
# 2𝑎
# Když je 𝐷 záporné, rovnice nemá žádné kořeny.
# Úkol:
# Ze vstupu načtěte koeficienty kvadratické rovnice 𝑎, 𝑏, 𝑐. Rovnici vyřešte a její kořeny
# vypište na výstup.
# Vypisujte s přesností na dvě desetinná místa. Když budou kořeny dva, vypište menší,
# # pak větší. Když nebude žádný kořen, vypište No solution

from math import sqrt

# Získání hodnot a, b, c na jednom řádku oddělených mezerou
a, b, c = map(float, input("Zadejte hodnoty a, b, c oddělené mezerou: ").split())

def kvadraticka_rovnice(a, b, c):
    # Ošetření, zda a není rovno nule
    if a == 0:
        print("Kvadratická rovnice není definována pro a = 0.")
        return

    # Výpočet diskriminantu
    D = b**2 - 4*a*c

    if D > 0:
        x_1 = (-b + sqrt(D))/(2*a)
        x_2 = (-b - sqrt(D))/(2*a)
        if x_1 > x_2:
            print(f"První kořen je {x_2} a druhý kořen je {x_1}")
        if x_2 > x_1:
            print(f"První kořen je {x_1} a druhý kořen je {x_2}")

    elif D == 0:
        x_1 = -b / (2*a)
        print(f"Jediný kořen je {x_1}")

    else:
        print("Kvadratická rovnice nemá reálná řešení.")
        real_part = -b / (2*a)
        imaginary_part = sqrt(-D) / (2*a)
        x_1 = complex(real_part, imaginary_part)
        x_2 = complex(real_part, -imaginary_part)

        return print(f"Prvni koren: {x_1} a druhy koren: {x_2}")
        


kvadraticka_rovnice(a, b, c)



