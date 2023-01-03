def calcule(num1,operator,num2):
    if operator == "+":
        return(print(num1+num2))
    
    elif operator == "-":
        return(print(num1-num2))

    elif operator == "*":
        return(print(num1*num2))

    elif operator == "/":
        return(print(num1/num2))

    elif operator == "%":
        return(print(num1%num2))

    
calcule(2,"+",2)
calcule(10,"-",2)
calcule(5,"*",5)
calcule(20,"/",2)
calcule(7,"%",3)