
# du_X_Y.py
# DÚ 5.2: Nejdelší a nejkratší slovo
# Ze vstupu načtěte slova a vypište nejkratší a nejdelší slovo.
# Vzorový vstup:
# pes kočka holub slepice sokol anaconda slon liška
# Vzorový výstup:
# anaconda
# pes

vstup = input("Napis libovolna slova: \n")

vstup = vstup.split()

slovo = "a"

for i in vstup:
    if len(slovo) >= len(i):

        slovo = slovo

    else:

        slovo = i

print(slovo)

for i in vstup:
    if len(slovo) <= len(i):

        slovo = slovo

    else:

        slovo = i

print(slovo)
