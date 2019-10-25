a, b, c, d = list(map(int, input().split()))
def euqlid(x,y):
    if x < y :
        temp = x
        x = y
        y = temp
    while x % y != 0:
        temp = x
        x = y
        y = temp % y
    return y
def searchCount(p,q,k):
    min = 0
    max = 0
    if p % k == 0:
        min = p // k
    else:
        min = p//k + 1
    max = q//k
    return max - min + 1
lcm = euqlid(c,d)
gcd = int((c * d) / lcm)
print((b - a + 1) - searchCount(a,b,c) - searchCount(a,b,d) + searchCount(a,b,gcd))
