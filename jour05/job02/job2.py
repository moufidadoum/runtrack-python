def rectangle(widht,height):
    resultat = "|-------------|\n|           |\n"
    for i in range(height):
        for j in range(widht):
            if i == 0 or i == height -1:
            
                print("-", end="")
            elif j == 0 or j == widht -1:
                print("|", end="")
            else:
                print(" ", end="")
print()


