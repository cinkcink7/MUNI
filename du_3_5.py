
# du_X_Y.py

# DÚ 3.5: DNA podruhé
# Relativní četnost báze vyjádřuje, jaká část sekvence (kolik procent) je tvořena daným
# typem báze.
# Úkol:
# Ze standardního vstupu načtěte sekvenci DNA. Na výstup vypište relativní četnosti
# jednotlivých bazí v procentech. Zaokrouhlujte na celá procenta.
# Poznámka: Formát .0% zde nebude fungovat, protože vypisuje procenta bez mezery.
# Musíte si poradit jinak.
# Vzorový vstup 1:   Vzorový vstup 2:  
# ACGTTTTGAG AAAACCCCTTTTTTTTTT
# Vzorový výstup 1:   Vzorový výstup 2:  
# A: 20 % A: 22 %
# C: 10 % C: 22 %
# G: 30 % G: 0 %
# T: 40 % T: 56 


# varA
# sekvence = input("Zadej retezec DNA: \n")

# aa = sekvence.count("A")
# tt = sekvence.count("T")
# cc = sekvence.count("C")
# gg = sekvence.count("G")
# celkem = aa + tt + cc + gg 
# a = 100* aa // celkem 
# t = 100* tt // celkem
# c = 100* cc // celkem
# g = 100* gg // celkem
# # print(f"A : {a} C : {c} G : {g} T : {t}")
# print(f"A : {a} %\nC  : {c} %\nG  : {g} %\nT : {t} %")



# varB
sequence = input()  # Načte sekvenci DNA ze vstupu

# Inicializuje slovník pro ukládání četností
base_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

# Prochází sekvenci a počítá četnosti
for base in sequence:
    if base in base_counts:
        base_counts[base] += 1

# Celková délka sekvence
sequence_length = len(sequence)

# Vypíše relativní četnosti v procentech
for base, count in base_counts.items():
    relative_frequency = (count / sequence_length) * 100
    print(f"{base}: {int(round(relative_frequency))} %")
