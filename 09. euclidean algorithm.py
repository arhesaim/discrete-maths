a = 2023
b = 28

# нод
def gcd(a, b):
    r = a%b

    q = int(a/b)

    while (r!=0):
        a = b
        b = r
        q = int(a/b)
        r = a - (b*q)
    return b

#  нок
def lcm(gcd, a, b):
    return a/gcd*b
    

print(gcd(a,b))
print(lcm(gcd(a,b), a, b))