
# du_X_Y.py
# DÚ 4.4: Caesarova šifra
# Caesarova šifra spočívá v posunu každého písmena o pevný počet pozic v abecedě.
# Tento počet se nazývá klíč.
# Například je-li klíč 2, pak posouváme o 2 pozice doprava a písmeno B se změní na D.
# Zpráva Hello World se zašifruje na Jgnnq Yqtnf. Když chceme zprávu rozšifrovat,
# musíme ji posunout o stejný počet pozic zpátky doleva.
# Záporný klíč znamená posun opačným směrem, tj. zašifrování doleva, rozšifrování
# doprava.

# Na vstupu získate klíč a zašifrovanou zprávu (mezi nimi znak #). Zprávu rozšifrujte a
# vypište.
# Mezery mezi písmeny nechte beze změny. Ke kódování používáme standardní anglickou abecedu, která má pořadí 
# stejné jako znakové sady ASCII nebo Unicode.
# Nemusíte řešit přetečení (tj. že například znak Z by se posunul zpátky na začátek
# abecedy na B).
# Nápověda: Použijte funkce chr a ord (viz konec přednášky Řetězce). Při výpisu
# můžete využít funkci print s parametrem end='' (nezalamuje výstup na nové řádky).
# Vzorový vstup 1:   Vzorový vstup 2:  
# 5#Rfrf rjqj rfxt -3#Sbkhr gb sbqokl
# Vzorový výstup 1:   Vzorový výstup 2:  
# Mama mele maso      Venku je vetrno

""" 
def caesar_sifra(text, klic):
    zasifrovany_text = ""
    klic = int(klic)  # Převod klíče na celé číslo

    for pismeno in text:
        if pismeno.isalpha():
            if pismeno.islower():
                zasifrovany_pismeno = chr(((ord(pismeno) - ord('a') + klic) % 26) + ord('a'))
            else:
                zasifrovany_pismeno = chr(((ord(pismeno) - ord('A') + klic) % 26) + ord('A'))
        else:
            zasifrovany_pismeno = pismeno

        zasifrovany_text += zasifrovany_pismeno

    return zasifrovany_text

retezec = input("Zadej klic a text oddeleny '#' znakem: ")
klic, text = retezec.split('#')

zasifrovany_text = caesar_sifra(text, klic)
print("Zašifrovaný text:", zasifrovany_text)

rozsifrovany_text = caesar_sifra(zasifrovany_text, -int(klic))
print("Rozšifrovaný text:", rozsifrovany_text)
 """
# Jgnnq Yqtnf
#########################################################################################
# def rozsifruj_zpravu(klic, zprava):
#     rozsifrovana_zprava = ""

#     for pismeno in zprava:
#         if pismeno.isalpha():
#             if pismeno.islower():
#                 rozsifrovane_pismeno = chr(((ord(pismeno) - ord('a') - int(klic)) % 26) + ord('a'))
#             else:
#                 rozsifrovane_pismeno = chr(((ord(pismeno) - ord('A') - int(klic)) % 26) + ord('A'))
#         else:
#             rozsifrovane_pismeno = pismeno

#         rozsifrovana_zprava += rozsifrovane_pismeno

#     return rozsifrovana_zprava

# vstup = input("Zadej klíč a zašifrovanou zprávu oddělenou '#': ")
# klic, zprava = vstup.split('#')

# rozsofrovana_zprava = rozsifruj_zpravu(klic, zprava)
# print(rozsofrovana_zprava)

# #-3#Sbkhr gb sbqokl

##############################################################################################################

# var b


# Načtěte vstupní klíč a zašifrovanou zprávu oddělenou znakem #
input_str = input("Zadejte klíč a zašifrovanou zprávu (oddělené #): ")

# Rozdělení vstupu na klíč a zašifrovanou zprávu
key, encrypted_message = input_str.split("#")

# Převedení klíče na celé číslo
shift = int(key)

# Inicializace proměnné pro dešifrovanou zprávu
decrypted_message = ""

# Projděte zašifrovanou zprávu a dešifrujte ji
for char in encrypted_message:
    if char.isalpha():
        # Rozhodněte, zda je znak velký nebo malý
        is_upper = char.isupper()
        
        # Převeďte znak na hodnotu Unicode
        char_code = ord(char)
        
        # Posuňte znak o hodnotu klíče
        char_code -= shift
        
        # Pokud znak přesáhl hranici písmen, upravte jej
        if is_upper:
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code < ord('a'):
                char_code += 26
        
        # Převeďte znak zpět na písmeno
        decrypted_char = chr(char_code)
        
        # Přidejte písmeno do dešifrované zprávy
        decrypted_message += decrypted_char
    else:
        # Zachovejte mezery a další znaky beze změny
        decrypted_message += char

# Výstup dešifrované zprávy
print(decrypted_message)
