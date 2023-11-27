# # print(100//33)
# # print(100/33)
# #print(100%33)


# def select_even(numbers: list[int]) -> list[int]:
#     # vypise suda cisla v listu
#     result = []
#     for x in numbers:
#         if x % 2 == 0:
#             result.append(x)
#     return result



# # print(select_even([12, 44, 77]))

# ############################################################

# def select_odd(numbers: list[int]) -> list[int]:
#     # vypise licha cisla
#     result = []
#     for x in numbers:
#         if x % 2 != 0:
#             result.append(x)
#     return result

# # print(select_odd([12, 44, 77]))

# ########################################################

# def main() -> None:
#     numbers = input('Input numbers: ').split()

#     even_numbers = select_even(numbers)
#     odd_numbers = select_odd(numbers)
    
#     print('Even numbers:', ', '.join(even_numbers))
#     print('Odd numbers:', ', '.join(odd_numbers))


# main()

#####################################################33^^^^^^^^^^^^^^^^^^^^^^^^^^

def select_even(numbers: list[int]) -> list[int]:
    result = []
    for x in numbers:
        if x % 2 == 0:
            result.append(x)
    return result


def select_odd(numbers: list[int]) -> list[int]:
    result = []
    for x in numbers:
        if x % 2 != 0:  # Oprava pro výběr lichých čísel
            result.append(x)
    return result


def main() -> None:
    numbers = list(map(int, input('Input numbers: ').split()))

    even_numbers = select_even(numbers)
    odd_numbers = select_odd(numbers)
    
    print('Even numbers:', ', '.join(map(str, even_numbers)))
    print('Odd numbers:', ', '.join(map(str, odd_numbers)))


if __name__ == '__main__':
    main()
