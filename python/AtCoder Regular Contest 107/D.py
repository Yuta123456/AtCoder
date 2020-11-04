n, k = map(int, input().split())
ans = 0
mod = 998244353
ball = k * 2
pole = n-1
fact = [0 for i in range(6001)]
fact[0] = 1
for i in range(1,6001):
    fact[i] = (fact[i-1] * i) % mod
ans = fact[pole + ball] * pow(fact[pole], -1, mod) * pow(fact[ball], -1, mod)
print(ans % mod)