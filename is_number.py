
# du_X_Y.py
# Úkoly v této sadě řešte do připravených souborů is_number.py, mean.py,
# patients.py, triangles.py, které pak odevzdáte do odevzdávárny. Doctesty 
# a typové anotace v těchto souborech považujte za součást zadání (proto v tomto zadání
# nejsou vzorové vstupy a výstupy ani testovací buňky).
# Doctesty spustíte z příkazové řádky:
# python -m doctest ***.py # default mode
# python -m doctest ***.py -v # verbose mode
# Úkoly 8.4, 8.5, 8.6 na sebe navazují, tj. v každém dalším úkolu se očekává využití
# funkcí implementovaných v předchozích úkolech.
# DÚ 8.1: Je to číslo?
# V souboru is_number.py doplňte funkci is_number, která bere jako parameter
# řetězec a vrací hodnotu True, pokud tento řetězec je validním zápisem reálného čísla,
# False v opačném případě.

#varA
# def is_number(vstup):

#     if isinstance(vstup,(int, float)):
#         return True
    
#     else:
#         return False

# print(is_number(16464))
# print(is_number("pavel"))
# print(is_number("1.555"))
####################################################################################

# VarB

def is_number(vstup):
    try:
        transformace = float(vstup)
        vstup = transformace
        return True
    except ValueError:
        return False

# print(is_number(16464))  # Vrací True
# print(is_number("pavel"))  # Vrací Falset"
# print(is_number("1.555"))  # Vrací True