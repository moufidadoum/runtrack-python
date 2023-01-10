L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

product = 1

for x in L:
    if 25 <= x <= 90:
        product *= x
print(f"Le produit des valeurs entre 25 et 90 est {product}.")
