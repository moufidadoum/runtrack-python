L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]


somme_valeurs_paires = 0
for x in L:
    if x % 2 == 0:
        somme_valeurs_paires += x
print(f"La somme des valeurs paires de la liste est {somme_valeurs_paires}.")