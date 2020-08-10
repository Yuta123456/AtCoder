from collections import defaultdict
factor = defaultdict(int)

a,b = map(int, input().split())

for i in range(b+1,a+1):
#for i in range(5,10):
    num = i
    for div in range(2,int(i**0.5) + 1):
        div_count = 0
        while num % div == 0:
            div_count += 1 
            num = num // div
        if div_count != 0:
            factor[div] += div_count
    if num != 1:
        factor[num] += 1
ans = 1
mod = 10**9+7
for i in factor.values():
    ans *= i + 1
    ans %= mod
print(ans)