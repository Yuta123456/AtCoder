from fractions import gcd
n = int(input())
for i in range(n):
    t = int(input())
    if i == 0:
        l = t
        k = t
    else:
        l = gcd(k, t)
        k = k * t//l
print(k)