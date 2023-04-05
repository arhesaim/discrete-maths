#5 вариант

def conjuction(x, y):
    if (x == y == 0 or x != y):
        return 0
    elif (x==y==1):
        return 1
    

def equivalence(x, y):
    if (x==y==0 or x==y==1):
        return 1
    else: 
        return 0

def comparison(x,y,z):
    for i in range(len(x)):
        fResult = conjuction(x[i], equivalence(y[i], z[i]))
        sResult = equivalence(equivalence(conjuction(x[i], y[i]), conjuction(x[i], z[i])), x[i])
        if (fResult == sResult):
            print(fResult, "==", sResult)
        else: print(fResult, "!=", sResult)

if __name__ == "__main__":
    x = [0,0,0,0,1,1,1,1]
    y = [0,0,1,1,0,0,1,1]
    z = [0,1,0,1,0,1,0,1]
    comparison(x,y,z)