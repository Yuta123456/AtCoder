n = int(input())
a = list(map(int, input().split()))
min_card = min(a)
ans = min_card
from math import gcd
for i in range(n):
    ans = gcd(ans, a[i])
print(ans)