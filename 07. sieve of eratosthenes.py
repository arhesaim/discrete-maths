import math

n = 200
array = []

for i in range(n):
    if (i < 2):
        array.append(False)
    else:
        array.append(True)


for i in range(0, int(math.sqrt(n))+1):
    if array[i] == True:
        k = 1
        sk = i*i
        for j in range(i*i, n, i*k):
            if j == sk:
                array[j] = False
                continue
            else: 
                array[j] = False
                k+= 1

for i in range(n):
    if array[i] == True:
        print(i)