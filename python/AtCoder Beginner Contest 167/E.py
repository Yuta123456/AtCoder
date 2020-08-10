import sys
sys.setrecursionlimit(10**6)
n,m,k = map(int, input().split())
mod = 998244353
ans = 0
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
combi = [0 for i in range(n)]
combi[0] = 1
for i in range(1,n):
    combi[i] = (combi[i-1]*(n-i)*mod_inv(i,mod)) % mod
for i in range(k+1):
    plus = m * pow(m-1,n-1-i,mod)
    plus *= combi[n-i-1]
    plus %= mod
    ans += plus
    ans %= mod
print(ans)