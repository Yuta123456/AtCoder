import math
x,y = list(map(int, input().split()))
mod = 7 + (10**9)
ans = 0
factorial = [1]*(x+y)

for i in range(1,max(x,y)):
    factorial[i] = (factorial[i - 1] * i) % mod
for i in range(y + 1):
    if (2 * x) - (y) == 3 * i:
        k = x - 2 * i
        if k < 0:
            continue
        ans += factorial[k + i] / (factorial[k] * factorial[i])
#逆元の探索
for i in range():
print(int(ans))