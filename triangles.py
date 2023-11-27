
def triangle_area(a: float, b: float, c: float) -> float:
    """Vrať povrch trojúhelníku se stranami a, b, c. Vyhoď ValueError pokud strany nesplňují trojúhelníkovou nerovnost.
    >>> round(triangle_area(3, 4, 5), 6)
    6.0
    >>> round(triangle_area(5.4, 5.2, 5.3), 6)
    12.154663
    >>> round(triangle_area(3, 4, 8), 6)
    Traceback (most recent call last):
        ...
    ValueError: Violating triangle inequality
    >>> round(triangle_area(3, 2, 1), 6)
    Traceback (most recent call last):
        ...
    ValueError: Violating triangle inequality
    >>> round(triangle_area(1.5, 2, 0.3), 6)
    Traceback (most recent call last):
        ...
    ValueError: Violating triangle inequality
    """
    raise NotImplementedError()


def largest_triangle(triangles: list[tuple[float, float, float]]) -> tuple[float, float, float]:
    """Vyber trojúhelník s největším obsahem.
    >>> largest_triangle([(3, 4, 5), (3, 4, 8), (6, 7, 6)])
    (6, 7, 6)
    >>> largest_triangle([(1, 2, 3)])
    Traceback (most recent call last):
        ...
    ValueError: No valid triangles
    """
    raise NotImplementedError()


def largest_triangle_io(input_line: str) -> str:
    """Zpracuj vstupní řetězec se zápisem trojúhelníků a vrať řetězec s hlášením o největším trojúhelníku.
    >>> largest_triangle_io('3.0-4.0-5.0; 3-4-8; 6-7-6')
    'Largest triangle is: 6.00-7.00-6.00'
    >>> largest_triangle_io('1-2-3; 4.5-8-16')  # Všechny trojúhelníku porušují troj. nerovnost
    'No valid triangles'
    >>> largest_triangle_io('3-4-5a; 8-7-10')  # 5a není správné číslo
    'Invalid input'
    >>> largest_triangle_io('3-4-5; 8-8; 42-42-42')  # Druhý trojúhelník má zadané pouze 2 strany
    'Invalid input'
    """
    raise NotImplementedError()


def main() -> None:
    """Načti ze vstupu zápis trojúhelníku, a vypiš hlášení o největším trojúhelníku."""
    inp = input('Zadejte délky stran trojúhelníků (např. "3-4-5; 1.2-2-1.5"): ')
    out = largest_triangle_io(inp)
    print(out)


if __name__ == '__main__':
    main()
    

################################################################################################

#VAR A

# from typing import List, Tuple


# def triangle_area(a: float, b: float, c: float) -> float:
#     """Vrať povrch trojúhelníku se stranami a, b, c. Vyhoď ValueError pokud strany nesplňují trojúhelníkovou nerovnost."""
#     if a + b <= c or a + c <= b or b + c <= a:
#         raise ValueError("Violating triangle inequality")
    
#     s = (a + b + c) / 2
#     area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#     return area


# def largest_triangle(triangles: List[Tuple[float, float, float]]) -> Tuple[float, float, float]:
#     """Vyber trojúhelník s největším obsahem."""
#     if not triangles:
#         raise ValueError("No valid triangles")
    
#     max_area = 0
#     largest = None

#     for triangle in triangles:
#         try:
#             area = triangle_area(*triangle)
#             if area > max_area:
#                 max_area = area
#                 largest = triangle
#         except ValueError:
#             pass
    
#     if largest is None:
#         raise ValueError("No valid triangles")
    
#     return largest


# def largest_triangle_io(input_line: str) -> str:
#     """Zpracuj vstupní řetězec se zápisem trojúhelníků a vrať řetězec s hlášením o největším trojúhelníku."""
#     triangles = input_line.split("; ")
#     triangle_list = []

#     for triangle in triangles:
#         sides = triangle.split("-")
#         if len(sides) != 3:
#             return "Invalid input"
        
#         try:
#             a, b, c = map(float, sides)
#             triangle_list.append((a, b, c))
#         except ValueError:
#             return "Invalid input"

#     try:
#         largest = largest_triangle(triangle_list)
#         return f"Largest triangle is: {'-'.join(f'{side:.2f}' for side in largest)}"
#     except ValueError as e:
#         return str(e)


# def main() -> None:
#     """Načti ze vstupu zápis trojúhelníku, a vypiš hlášení o největším trojúhelníku."""
#     inp = input('Zadejte délky stran trojúhelníků (např. "3-4-5; 1.2-2-1.5"): ')
#     out = largest_triangle_io(inp)
#     print(out)


# if __name__ == '__main__':
#     main()

############################################################################################################
############################################################################################################
############################################################################################################
#VAR B uloha 8.4 a

def triangle_area(a: float, b: float, c: float) -> float:
    """Vrať povrch trojúhelníku se stranami a, b, c. Vyhoď ValueError pokud strany nesplňují trojúhelníkovou nerovnost."""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Violating triangle inequality")
    
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

##############################################################################################################

#VAR B  uloha 8.5 a

def triangle_area(a: float, b: float, c: float) -> float:
    """Vrať povrch trojúhelníku se stranami a, b, c. Vyhoď ValueError pokud strany nesplňují trojúhelníkovou nerovnost."""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Violating triangle inequality")
    
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def largest_triangle(triangles: list[tuple[float, float, float]]) -> tuple[float, float, float]:
    """Vyber trojúhelník s největším obsahem."""
    largest_area = 0
    largest_triangle = None
    valid_triangle = False
    
    for triangle in triangles:
        try:
            a, b, c = triangle
            area = triangle_area(a, b, c)
            if area > largest_area:
                largest_area = area
                largest_triangle = triangle
                valid_triangle = True
        except ValueError:
            pass
    
    if not valid_triangle:
        raise ValueError("No valid triangles")
    
    return largest_triangle


#########################################################################################################


# VAR B 8.6 a

def triangle_area(a: float, b: float, c: float) -> float:
    """Vrať povrch trojúhelníku se stranami a, b, c. Vyhoď ValueError pokud strany nesplňují trojúhelníkovou nerovnost."""
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Violating triangle inequality")
    
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

def largest_triangle(triangles: list[tuple[float, float, float]]) -> tuple[float, float, float]:
    """Vyber trojúhelník s největším obsahem."""
    largest_area = 0
    largest_triangle = None
    valid_triangle = False
    
    for triangle in triangles:
        try:
            a, b, c = triangle
            area = triangle_area(a, b, c)
            if area > largest_area:
                largest_area = area
                largest_triangle = triangle
                valid_triangle = True
        except ValueError:
            pass
    
    if not valid_triangle:
        raise ValueError("No valid triangles")
    
    return largest_triangle

def largest_triangles_io(input_line: str) -> str:
    """Zpracuj vstupní řetězec se zápisem trojúhelníků a vrať řetězec s hlášením o největším trojúhelníku."""
    triangles = [tuple(map(float, triangle.split('-'))) for triangle in input_line.split(';')]
    
    try:
        largest = largest_triangle(triangles)
        return f"Largest triangle is: {'-'.join([f'{side:.2f}' for side in largest])}"
    except ValueError as e:
        return str(e)

def main() -> None:
    """Načti ze vstupu zápis trojúhelníku, a vypiš hlášení o největším trojúhelníku."""
    inp = input('Zadejte délky stran trojúhelníků (např. "3-4-5; 1.2-2-1.5"): ')
    out = largest_triangles_io(inp)
    print(out)

if __name__ == '__main__':
    main()
#############################################################################################
#############################################################################################
#############################################################################################

