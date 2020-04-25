import math
n,k = map(int, input().split())
mod = 10**9 + 7
ans = 1
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

if n <= k:
    remain = k % n
    #nCremain
    for i in range(1,remain+1):
        ans *= (n - i + 1) * mod_inv(i,mod)
        ans %= mod
    print(ans)
else:
    #重複組み合わせ
    a = math.factorial(n-1+k)
    b = math.factorial(n-1) * math.factorial(k)
    a %= mod
    b %= mod
    ans = a * mod_inv(b,mod)
    print(ans % mod)
