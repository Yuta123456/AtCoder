from math import gcd
import math
n, k= map(int, input().split())
mod = 10**9+7
#全ての倍数の数を求める
ans = 0
count = [0 for i in range(k+1)]
for i in range(k,0,-1):
    num = k // i
    count[i] = pow(num,n,mod) 
    for j in range(i*2,k+1,i):
        count[i] -= count[j]
    ans += (count[i] * i)
    ans %= mod
print(ans)


