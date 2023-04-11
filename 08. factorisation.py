import math

def fermat_factor(num):
    for q in range(1, int(((num-1)/2)+1), 1):
        p2 = q*q + num
        if (math.sqrt(p2)%int(math.sqrt(p2))==0):
            div1 = math.sqrt(p2) - q
            div2 = math.sqrt(p2) + q
            if (div1 == float(nums[i]) or div1 == float(1)):
                print(nums[i], "prime num, divides by: ", div1, div2)
                break
            else:
                print(nums[i], "not a prime num divides by: ", div1, div2)
                break
        else: continue

if __name__ == "__main__"  :
    nums = [40, 13, 19, 67, 45]
    for i in range(len(nums)):
        fermat_factor(nums[i])        