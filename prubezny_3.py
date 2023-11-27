# print("Hallo World!")

# Úkol 3 (10 bodů)
# Doplňte funkci filter_first_quadrant, která vezme seznam bodů v rovině (každý
# bod je reprezentován dvojicí souřadnic (𝑥, 𝑦)) a vrátí přefiltrovaný seznam obsahující
# pouze body, které leží v I. kvadrantu (body oranžovou barvou). Pro body v I. kvadrantu
# platí 𝑥 > 0, 𝑦 > 0.


def filter_first_quadrant(points):
    # Inicializace prázdného seznamu pro filtrované body
    filtered_points = []
    
                            
    for x, y in points:# Procházení bodů a filtrování těch v I. kvadrantu
        if x > 0 and y > 0:
            filtered_points.append((x, y))
    
    return filtered_points

# Vstupní seznam bodů
points = [(2, 2), (-0.5, -0.5), (0.5, 0.9), (1.5, -3.5), (-3.5, 1.5), (-2, 2), (3, -2), (-1, -1), (0, 0)]

# Volání funkce pro filtrování bodů v I. kvadrantu
filtered_points = filter_first_quadrant(points)

# Výpis filtrovaných bodů
print(filtered_points)


