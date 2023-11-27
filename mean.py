
# du_8_1

# V souboru mean.py doplňte funkci mean, která vezme seznam čísel a vrátí jejich
# průměr.
# Zamyslete se nad tím, jaké problémy by mohly během výpočtu nastat, a napište funkci
# tak, aby neskončila chybou. Pokud průměr nelze spočítat, vraťte hodnotu math.nan
# (not a number).

#ZADANI
# def mean(numbers: list[float]) -> float:
#     """Vrať průměr čísel `numbers`.
#     >>> round(mean([1, 2]), 6)
#     1.5
#     >>> round(mean([1, 2, 4]), 6)
#     2.333333
#     >>> round(mean([0.5, -10, 12.5, 9, 9.156, -3.2]), 6)
#     2.992667
#     >>> round(mean([]), 6)
#     nan
#     """
#     raise NotImplementedError()

##################################################################################################
# VarA testovani zdali je to proveditelne

# import unittest

# def mean(numbers):
#     return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# class TestMeanFunction(unittest.TestCase):
    
#     def test_mean(self):
#         # Test průměru seznamu float čísel
#         self.assertAlmostEqual(mean([1.5, 2.5]), 2.0)  # Očekává se průměr 2.0

# if __name__ == '__main__':
#     unittest.main()

# VarA_2_testovani zdali je to float v zadani

# import unittest

# def mean(numbers):
#     if not all(isinstance(num, float) for num in numbers):
#         raise ValueError("Všechny hodnoty v seznamu musí být typu float")
#     return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# class TestMeanFunction(unittest.TestCase):
    
#     def test_all_float_values(self):
#         # Test, zda funkce mean vyvolá ValueError, pokud nejsou všechny hodnoty typu float
#         with self.assertRaises(ValueError):
#             mean([1, 2, 3])  # Hodnoty nejsou typu float

#         # Test, kdy jsou všechny hodnoty typu float
#         self.assertAlmostEqual(mean([1.5, 2.5]), 2.0)  # Očekává se průměr 2.0

# if __name__ == '__main__':
#     unittest.main()

####################################################################################################

# VarB vlastni funkce s erorama co napadnou

# def mean(numbers: list[float], pocet_mist_zaokr) -> float:
#     #vrati prumer cisel "numbers"
#     try:
#         delka_listu = len(numbers)
#         suma = 0
#         for i in numbers:
#             suma = suma + i

#         prumer = round(suma / delka_listu, pocet_mist_zaokr)
#         return prumer
    
#     except ZeroDivisionError:

#         print("nelze delit nulou")

# print(mean([2, 6, 1, 100], 5))
# print(mean([2, 4, 1], 5))
# print(mean([], 6))

#####################################################################
# varC snad lepsi varianta B
#  >>> round(mean([]), 6)
#     nan
#     """
#     raise NotImplementedError()


def mean(numbers: list[float], pocet_mist_zaokr) -> float:
    #vrati prumer cisel "numbers"
    
    delka_listu = len(numbers)
    suma = 0
    
    for i in numbers:
        suma = suma + i

    prumer = round(suma / delka_listu, pocet_mist_zaokr)
    return prumer
    


def vyjimka_na_deleni_nulou(numbers: list[float], pocet_mist_zaokr) -> float:
    #vyhodi vyjimku pokud budeme delit nulou
    
    if len(numbers) == 0:
        raise ValueError("Dělení nulou není povoleno")
    return suma / len(numbers)


print(mean([2, 6, 1, 100], 5))
print(mean([2, 4, 1], 5))
# print(mean([], 6))

# def divide(x, y):
#     if y == 0:
#         raise ValueError("Dělení nulou není povoleno")
#     return x / y

# # Příklad volání funkce divide s různými parametry
# try:
#     result = divide(10, 0)
#     print("Výsledek dělení:", result)
# except ValueError as e:
#     print("Došlo k chybě:", str(e))
