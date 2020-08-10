import math
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
mod = 10**9 + 7
def mod_factorial(n):
    ans = 1
    while n >= 2:
        ans  = (ans * n) % mod
        n -= 1
    return ans
if abs(n - m) == 1:
    print((mod_factorial(n) * mod_factorial(m)) % mod)
elif abs(n - m) == 0:
    print((mod_factorial(n) * mod_factorial(m) * 2) % mod)
else:
    print(0)