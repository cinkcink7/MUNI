
# # du_X_Y.py
# Cvičení 5.4: Čísla, čísla, čísla
# Úkol:
# Na vstupu získáte posloupnost čísel oddělených mezerou. Spočítejte a vypište minimum, maximum, aritmetický průměr a medián.
# Vypisované hodnoty zarovnejte napravo, viz vzorový výstup (na každém řádku je
# dohromady 14 znaků).
# Vzorový vstup 1:  
# 2
# 150 13 7 10 11
# Vzorový výstup 1:  
# Min: 7.00
# Max: 150.00
# Mean: 38.20
# Median: 11.00
# Vzorový vstup 2:  
# 1 2 3 4 8 9
# Vzorový výstup 2:  
# Min: 1.00
# Max: 9.00
# Mean: 4.50
# Median: 3.5
import statistics


vstup = input("Vstup: \n")
vstup = vstup.split()
vstup = [float(x) for x in vstup] # prevede strs v listu na intgs

Min = min(vstup)
Max = max(vstup)
Mean = sum(vstup)/len(vstup)
Median = statistics.median(vstup)

print(f" Min = {Min:.2f}")
print(f" Max = {Max:.2f}")
print(f" Mean = {Mean:.2f}")
print(f" Median = {Median:.2f}")