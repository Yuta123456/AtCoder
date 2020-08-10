n = int(input())
lst1 = list(map(int,input().split()))
mod = 10**9+7

import fractions as math
#リスト l の最大公約数
def lcmlist(l):
    a = l[0]
    for i in range(len(l)):
        #change
        a = (a*l[i]) //math.gcd(a,l[i])
    return a

g = lcmlist(lst1)
ans = 0
for i in range(n):
    ans += g//lst1[i]%mod

print(ans%mod)


