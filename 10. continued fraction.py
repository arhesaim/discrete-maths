a = 649
b = 200
cf = []
while b != 0:
    cf.append(a//b)
    a, b = b, a%b
print(cf)