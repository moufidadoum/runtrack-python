def fruitslegumes(type,saison):
    if type == "fruits" and saison == "hiver" :
        print("orange,mandarine et kiwi")

    elif type == "fruits" and saison == "ete" :
        print("poire, fraise et cassis")

    elif type == "legume" and saison == "hiver" :
        print ("carotte, topinambour et endive")

    elif type == "legume" and saison == "ete" :
        print ("artichaud, aubergine et navet")

fruitslegumes("fruits","ete")
fruitslegumes("legume","ete")