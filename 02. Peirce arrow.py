def peirce_arrow(x, y):
    if (x == y == 1 or x != y):
        return 0
    elif (x == y == 0):
        return 1
    
x = [0,0,1,1]
y = [0,1,0,1]

for i in range(len(x)):
    print(x[i], " | ", y[i], " |  ", peirce_arrow(x[i], y[i]))