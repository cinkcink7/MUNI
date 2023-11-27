# print("Hallo World!")


# Úkol 2 (14 bodů)
# Genetický kód představuje soubor pravidel, podle kterých se genetická informace
# uložená v DNA převádí na primární strukturu proteinů, tj. na pořadí aminokyselin v
# proteinovém řetězci. Každá trojice za sebou jdoucích bazí (kodon) se přeloží na jednu
# aminokyselinu, např. kodon ATG se preloží na aminokyselinu methionin (M), kodony
# GCT, GCC, GCA a GCG se přeloží na aminokyselinu alanin (A). Speciální význam mají
# takzvané stop kodony (TAA, TAG, TGA), které se nepřeloží na žádnou aminokyselinu,
# ale místo toho ukončí proces translace.
# Příklad: DNA sekvence ATGGCTCCACTTGAGTTT se přeloží na protein MAPLEF:
# ATG GCT CCA CTT GAG TTT
# M A P L E F
# Příklad 2: DNA sekvence ATGGCTCCATAAGAGTTT se přeloží na protein MAP, protože
# čtvrtým kodonem je stop kodon TAA, který ukončí translaci:
# 2
# ATG GCT CCA TAA GAG TTT
# M A P !
# Úkol:
# Napište program, který ze vstupu načte řádek se sekvencí genu v DNA. Program
# tento gen přeloží do sekvence proteinu a vypíše ji na výstup. V konstantě CODE máte
# připravený standardní genetický kód (stop kodony jsou označeny znakem !).
# Vzorový vstup:
# ATGGCTCCACTTGAGTTT
# Vzorový výstup:
# MAPLEF


# Konstanta s genetickým kódem
CODE = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '!', 'TAG': '!',
    'TGC': 'C', 'TGT': 'C', 'TGA': '!', 'TGG': 'W',
}

# Načtení vstupu
dna_sekvence = input()

# Funkce pro překlad DNA do proteinu
def preklad_dna_v_protein(dna_sekvence):
    protein_sekvence = ''
    i = 0
    while i < len(dna_sekvence):
        kodon = dna_sekvence[i:i+3]
        aminokyselina = CODE.get(kodon, '')
        if aminokyselina == '!':
            break
        protein_sekvence += aminokyselina
        i += 3
    return protein_sekvence

# Překlad DNA do proteinu
protein_sekvence = preklad_dna_v_protein(dna_sekvence)

# Výstup
print(protein_sekvence)
