#5 вариант

def disjuction(x, y):
    if (x == y == 0):
        return 0
    elif (x == y == 1 or x != y):
        return 1
    
def imp(x, y):
    if (x == y == 0 or x == y == 1 or x>y):
        return 1
    elif (x<y):
        return 0
    
def inversion(x):
    if (x == 0):
        return 1
    elif (x == 1):
        return 0
    
def xor(x, y):
    if (x == y == 0 or x == y == 1):
        return 0
    elif (x != y):
        return 1
     
def truth_table(x,y,z):
    for i in range(len(x)):
        print(x[i], "|", y[i], "|", z[i], "|", imp(y[i], z[i]), "|", inversion(imp(y[i], z[i])), "|", disjuction(x[i], inversion(imp(y[i], z[i]))), "|", xor(disjuction(x[i], inversion(imp(y[i], z[i]))), y[i]))

if __name__ == "__main__":
    x = [0,0,0,0,1,1,1,1]
    y = [0,0,1,1,0,0,1,1]
    z = [0,1,0,1,0,1,0,1]
    truth_table(x,y,z)