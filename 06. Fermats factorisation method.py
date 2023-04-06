import math

def fermat_factor(num):
    # q = 1
    # t = True
    # while t:
    #     p2 = q*q + num
    #     if (math.sqrt(p2)%int(math.sqrt(p2))==0):
    #         t = False
    #         return p2, q
    #     else: q+= 1
    for q in range(1, int(((num-1)/2)+1), 1):
        p2 = q*q + num
        if (math.sqrt(p2)%int(math.sqrt(p2))==0):
            return p2, q
        else: continue



if __name__ == "__main__"  :
    nums = [1001, 1349, 4851, 2749, 2861, 97]
    for i in range(len(nums)):
        s1, s2 = fermat_factor(nums[i])
        div1 = math.sqrt(s1) - s2
        div2 = math.sqrt(s1) + s2
        if (div1 == float(nums[i]) or div1 == float(1)):
            print(nums[i], "prime num, divides by", div1, div2)
        else:
            print(nums[i], "not a prime num, divides by", div1, div2)