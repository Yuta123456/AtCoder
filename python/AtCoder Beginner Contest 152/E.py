#互いに素なa,bについて、a*x+b*y=1の一つの解
def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

def mod_inv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

import fractions
mod = (10**9)+ 7
n = int(input())
a = list(map(int, input().split()))
lcm = 1
for i in range(n):
    gcd = fractions.gcd(lcm, a[i])
    lcm *= a[i]
    lcm = lcm // gcd
lcm %= mod
ans = 0
for i in range(n):
    k = mod_inv(a[i], mod)
    ans += lcm * k
    ans %= mod
print(ans)