
# # du_X_Y.py
# # Nepovinné úkoly
# Cvičení 4.5: Výpočet mocniny pomocí cyklu
# Umocňování čísla 𝑧 na exponent 𝑒 lze rozepsat pomocí násobení: 𝑧
# 𝑒 = 𝑧 ⋅ 𝑧 ⋅ 𝑧 ⋅ ..., kde
# počet zetek je roven 𝑒.
# Úkol:
# Ze vstupu získejte dvě přirozená čísla 𝑧, 𝑒. Spočítejte a vypište mocninu 𝑧
# 𝑒
# .
# Úlohu řešte pomocí cyklu, bez použití operátoru ** nebo funkce pow.
# Vzorový vstup 1:   Vzorový vstup 2:  
# 2 3 3 10
# Vzorový výstup 1:   Vzorový výstup 2:  
# 8 59049


n, e =  map(int, input().split())

vystup = 1
for i in range (e):

    vystup = vystup * n

print(vystup)