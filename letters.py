
# Cvičení 8.3: Písmena
# V souboru letters.py doplňte funkci letter_to_number, která vezme písmeno a
# vrátí jeho pořadové číslo v anglické abecedě (využijte funkci ord). Funkce by měla
# fungovat stejně pro velká i malá písmena.
# Pokud funkce dostane nevhodný argument, musí vyhodit výjimku typu ValueError s
# příslušnou hláškou (viz doctesty).


# def letter_to_number(letter: str) -> int:
#     """Vrať pořadové číslo písmena (v anglické abecedě).
#     >>> letter_to_number('A')
#     1
#     >>> letter_to_number('a')
#     1
#     >>> letter_to_number('D')
#     4
#     >>> letter_to_number('z')
#     26
#     >>> letter_to_number('ch')
#     Traceback (most recent call last):
#         ...
#     ValueError: letter must be a string with exactly one character
#     >>> letter_to_number('ž')
#     Traceback (most recent call last):
#         ...
#     ValueError: ž is not in the English alphabet
#     >>> letter_to_number('9')
#     Traceback (most recent call last):
#         ...
#     ValueError: 9 is not in the English alphabet
#     """
#     raise NotImplementedError()


# varA 

def letter_to_number(letter: str) -> int:
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("letter must be a string with exactly one character")

    letter = letter.lower()
    if letter < 'a' or letter > 'z':
        raise ValueError(f"{letter} is not in the English alphabet")

    return ord(letter) - ord('a') + 1



###########################################################################3
# varB
# letter = input("Vstup: \n")
# letter = letter.upper()

# anglicka_abeceda = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'

# try:  
#     position = anglicka_abeceda.index(letter) + 1  
#     print(f"The position in the English alphabet is: {position}")
          
# except ValueError:   
#     print(f"{letter} ... Invalid input or not a letter from the English alphabet.")


