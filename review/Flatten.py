#互いに素なa,bについて、a*x+b*y=1の一つの解
def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    #[x,y]
    return [w[0],w[1]]

# aの逆元(mod m)を求める。(aとmは互いに素であることが前提)
#a/b = a*(b`)となるb`を求める
def mod_inv(a,mod):
    x = extgcd(a,mod)[0]
    return (mod+x%mod)%mod



n = int(input())
mod = 10**9 + 7
a = list(map(int, input().split()))
from fractions import gcd
#from math import gcd
lcm = 1
for i in range(n):
    temp = gcd(lcm,a[i]) % mod
    lcm = (a[i] * lcm) * mod_inv(temp, mod)
    lcm %= mod
ans = 0
for i in range(n):
    ans += lcm * mod_inv(a[i], mod)
    ans %= mod
print(ans)
