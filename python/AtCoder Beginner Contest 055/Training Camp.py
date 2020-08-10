n = int(input())
ans = 1
mod = 7 + 10 ** 9
for i in range(1,n+1):
    ans *= i
    ans %= mod
print(ans % mod)