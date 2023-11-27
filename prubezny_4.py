# print("Hallo World!")
# Úkol 4 (14 bodů)
# Prasátko Peppa má pytlík s 10 zelenými a 10 červenými kuličkami. Z pytlíku postupně
# vytahuje kuličky a počítá jaká je pravděpodobnost, že v prvních 𝑘 tazích vytáhne pouze
# zelené kuličky (𝑃𝑘
# ):
# V prvním tahu je pravděpodobnost vytažení zelené 𝑃1 =
# 10
# 20 = 0.5.
# Pak ale v pytlíku zůstane už jen 9 zelených (z 19), takže pravděpodobnost, že v prvním
# 4
# i druhém tahu vytáhne zelenou, je 𝑃2 = 𝑃1
# ⋅
# 9
# 19 ≈ 0.237.
# Pravděpodobnost, že v prvních třech tazích vytáhne jen zelené, je pak 𝑃3 = 𝑃2
# ⋅
# 8
# 18 ≈
# 0.105,
# a tak dále, až pravděpodobnost, že z prvních 10 budou všechny zelené, je 𝑃10 = 𝑃9
# ⋅
# 1
# 11 ≈
# 5.4 ⋅ 10−6
# .
# Úkol:
# Doplňte funkci peppa_probabilities, která vezme jako parametry počáteční
# počty zelených a červených kuliček 𝑛green, 𝑛red a vrátí seznam pravděpodobností
# [𝑃1
# , 𝑃2 … 𝑃𝑛green ].
# Vzorové volání:
# peppa_probabilities(10, 10)
# Vzorový výsledek:
# [0.5, 0.23684210526315788, 0.10526315789473684, 0.04334365325077399, 0.01625386996


def peppa_probabilities(n_green, n_red):
    probabilities = []
    total_balls = n_green + n_red
    
    for k in range(1, n_green + 1):
        probability = (n_green / total_balls)
        probabilities.append(probability)
        n_green -= 1
        total_balls -= 1
        
    return probabilities

n_green = 10
n_red = 10
result = peppa_probabilities(n_green, n_red)

print(result)
