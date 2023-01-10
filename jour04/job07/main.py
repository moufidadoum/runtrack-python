L = [8, 24, 48, 2, 16]
n = 0
for x in L:
    if x % 3 == 0:
        n += 1
print(f"Il y a {n} multiples de 3 dans la liste.")