"""
Opravte chyby v tomto programu.

Zadání: 
Spočítej a vypiš body mass index (BMI = (hmotnost v kg) / (výška v m)**2) všech pacientů ze seznamu patients.
U pacientů s BMI mimo normální rozsah (18.5–25) vypiš vykřičník.
Nakonec vypiš průměr a median BMI.

Očekávaný výstup:
Bob's BMI is: 27.7 !
Alice's BMI is: 21.8 
Cyril's BMI is: 22.8 
-----------------
Average BMI: 24.1
Median BMI:  22.8
"""


# BMI_OK_RANGE = (18.5, 25)  # Bezpečný rozsah BMI


# def calculate_bmi(weight: float, height: float) -> float:
#     """Spočítej BMI pacienta o hmotnosti `weight` (kg) a výšce `height` (m)."""
#     weight / (height ** 2)

# def is_bmi_ok(bmi: float) -> bool:
#     """Rozhodni jestli je BMI v bezpečném rozsahu."""
#     return BMI_OK_RANGE[0] <= bmi <= BMI_OK_RANGE[1]

# def main() -> None:
#     patients = [('Bob', 80, 1.7), ('Alice', 64.5, 1.72), ('Cyril', 74, 1,8)]  # Jméno, hmotnost a výška jednotlivých pacientů
#     bmis = []
#     for i in patients:
#         name, weight, height = patients[i]
#         bmi = calculate_bmi(height, weight)
#         if not is_bmi_ok(bmi):
#             warning = '!'
#         print('{name}'s BMI is: {bmi:.1f} {warning}')
#     average = sum(bmis) / len(bmis)
#     average = statistics.median(bmis)
#     print('-----------------')
#     print(f'Average BMI: {average:.1f}')
#     print(f'Median BMI:  {median:.1f}')


# if __name__ == '__main__':
#     main()



##########################################################################################3

#VAR A jen takovy muj koncept
#funguje to ale asi budou skucet

# from statistics import median

# def calculate_bmi(weight: float, height: float) -> float:
#     return weight / (height ** 2)

# def main():
#     # Data for patients (weight in kilograms, height in meters)
#     patients = {
#         'Bob': {'weight': 80, 'height': 1.75},
#         'Alice': {'weight': 60, 'height': 1.70},
#         'Cyril': {'weight': 75, 'height': 1.80}
#     }

#     bmis = []
#     for name, data in patients.items():
#         bmi = calculate_bmi(data['weight'], data['height'])
#         bmis.append(bmi)
#         status = "!" if bmi < 18.5 or bmi > 25 else ""
#         print(f"{name}'s BMI is: {bmi:.1f} {status}")

#     print("-----------------")
#     avg_bmi = sum(bmis) / len(bmis)
#     median_bmi = median(bmis)

#     print(f"Average BMI: {avg_bmi:.1f}")
#     print(f"Median BMI: {median_bmi:.1f}")

# if __name__ == "__main__":
#     main()


##########################################################################################

# VAR B .. S opravenymi chybami
import statistics

BMI_OK_RANGE = (18.5, 25)  # Bezpečný rozsah BMI


def calculate_bmi(weight: float, height: float) -> float:
    """Spočítej BMI pacienta o hmotnosti `weight` (kg) a výšce `height` (m)."""
    return weight / (height ** 2)  # Přidána návratová hodnota

def is_bmi_ok(bmi: float) -> bool:
    """Rozhodni jestli je BMI v bezpečném rozsahu."""
    return BMI_OK_RANGE[0] <= bmi <= BMI_OK_RANGE[1]

def main() -> None:
    patients = [('Bob', 80, 1.7), ('Alice', 64.5, 1.72), ('Cyril', 74, 1.8)]  # Jméno, hmotnost a výška jednotlivých pacientů
    bmis = []
    for patient in patients:
        name, weight, height = patient  # Opravení indexů v n-tici
        bmi = calculate_bmi(weight, height)  # Opravení pořadí parametrů
        warning = ''  # Přidání defaultní hodnoty pro warning
        if not is_bmi_ok(bmi):
            warning = '!'
        print(f"{name}'s BMI is: {bmi:.1f} {warning}")  # Oprava formátování a interpolace stringu
        bmis.append(bmi)  # Přidání BMI do seznamu

    average = sum(bmis) / len(bmis)
    median = statistics.median(bmis)  # Oprava jména proměnné

    print('-----------------')
    print(f'Average BMI: {average:.1f}')
    print(f'Median BMI:  {median:.1f}')


if __name__ == '__main__':
    main()



####
# doctesty
import statistics
import doctest

BMI_OK_RANGE = (18.5, 25)  # Bezpečný rozsah BMI


def calculate_bmi(weight: float, height: float) -> float:
    """Spočítej BMI pacienta o hmotnosti `weight` (kg) a výšce `height` (m).

    >>> calculate_bmi(80, 1.7)
    27.7
    >>> calculate_bmi(64.5, 1.72)
    21.8
    >>> calculate_bmi(74, 1.8)
    22.8
    """
    return weight / (height ** 2)


def is_bmi_ok(bmi: float) -> bool:
    """Rozhodni jestli je BMI v bezpečném rozsahu.

    >>> is_bmi_ok(22)
    True
    >>> is_bmi_ok(25.5)
    False
    """
    return BMI_OK_RANGE[0] <= bmi <= BMI_OK_RANGE[1]


def main() -> None:
    patients = [('Bob', 80, 1.7), ('Alice', 64.5, 1.72), ('Cyril', 74, 1.8)]
    bmis = []
    for patient in patients:
        name, weight, height = patient
        bmi = calculate_bmi(weight, height)
        warning = ''
        if not is_bmi_ok(bmi):
            warning = '!'
        print(f"{name}'s BMI is: {bmi:.1f} {warning}")
        bmis.append(bmi)

    average = sum(bmis) / len(bmis)
    median = statistics.median(bmis)

    print('-----------------')
    print(f'Average BMI: {average:.1f}')
    print(f'Median BMI:  {median:.1f}')


if __name__ == '__main__':
    main()

doctest.testmod()
