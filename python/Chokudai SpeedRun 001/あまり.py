n = int(input())
a = list(map(int, input().split()))
mod = 10**9 + 7
digit = 0
for i in range(n):
    digit += len(str(a[i]))
ans = 0
for i in range(n):
    digit -= len(str(a[i]))
    tmp = a[i] * pow(10,digit,mod)
    ans += tmp
    ans %= mod
print(ans)
