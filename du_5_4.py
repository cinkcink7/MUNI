
# du_X_Y.py

# DÚ 5.4: Oko
# Ve hře Oko (Blackjack) je cílem získat co největší počet bodů, ne však víc než 21.
# Přitom karty 2 až 10 mají svou vlastní hodnotu; karty J, Q, K mají hodnotu 10; A má
# hodnotu 11.
# Příklady:
# • Mám-li na ruce karty 3, 5, K, 2, pak mám 3+5+10+2 = 20 bodů.
# • Mám-li na ruce karty 6, J, A, pak mám 0 bodů, protože 6+10+11 = 27, což je víc
# než 21.
# Úkol:
# Na vstupu získáte posloupnost karet oddělených čárkami. Spočítejte, za kolik bodů
# se tyto karty počítají, a výsledek vypište na výstup.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 2, 3, 5, K 6, J, A
# Vzorový výstup 1:   Vzorový výstup 2:  
# 2
# 20 0

# Var A

hodnoty_karet = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "A":11,"J":10, "Q":10, "K":10}

karty_v_ruce = input("Zadej karty co mas v ruce, oddeluj to carkou: \n")
karty_v_ruce = karty_v_ruce.split(", ")
celkova_hodnota_v_ruce = 0

for karta in karty_v_ruce:

    celkova_hodnota_v_ruce = celkova_hodnota_v_ruce + hodnoty_karet[karta]

print(celkova_hodnota_v_ruce)


