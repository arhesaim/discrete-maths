import math

def prime_num_check(num):
    k = int(math.sqrt(num))
    for i in range(2, k+1):
        if (i != 2 and i%2 == 0 and i != k):
            continue
        else:
            if (num%i != 0 and i != k):
                continue
            elif (num%i == 0):
                return False
            elif (i == k):
                return True   
            # else: continue           

if __name__ == "__main__":
    for i in range(4, 101, 1):
        if (prime_num_check(i)):
            print(i, end= ", ")