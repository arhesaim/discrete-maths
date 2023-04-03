def sheffer_stroke(x, y):
    if (x == y == 0 or x != y):
        return 1
    elif (x == y == 1):
        return 0

x = [0,0,1,1]
y = [0,1,0,1]

for i in range(len(x)):
    print(x[i], " | ", y[i], " |  ", sheffer_stroke(x[i], y[i]))