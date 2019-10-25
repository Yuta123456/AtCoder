import math
s = int(input())
r = math.floor(math.sqrt(s)) + 1
k = r**2 - s
if r == 10**9 + 1:
    print("{} {} {} {} {} {}".format(0, 0, 1,r - 1,r - 1, 0))
    exit()
def search_prime(k):
    p = math.floor(math.sqrt(k))
    for i in range(2,p + 1):
        if k % i == 0:
            return i
    return 1
prime = search_prime(k)
print("{} {} {} {} {} {}".format(0, 0, prime,r,r, int(k / prime)))
