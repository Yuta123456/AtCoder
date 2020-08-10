import math
n,k = map(int, input().split())
mod = 10**9+7
ans = 0
array = [i for i in range(n+1)]
first_sum = sum(array[:k])
latter_sum = sum(array[-k:])
for i in range(k,n+1):
    ans += (latter_sum - first_sum) + 1
    first_sum += array[i]
    latter_sum += array[-(i+1)]
    ans %= mod
ans += 1
print(ans % mod)