r,c = map(int, input().split())
x,y = map(int, input().split())
d,l = map(int, input().split())
mod = 10**9+7
ans = 0
import math
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
count = ( r + 1 - x ) * ( c + 1 - y )
dp = [[[0 for i in range(l+1)] for j in range(d+1)] for k in range(x*y+1)]
#dp[i][j][k] := i個めのマスまで考えて、机をj個、サーバをk個使った時の総数
for i in range(x*y+1):
    dp[i][0][0] = 1
for i in range(x*y):
    for j in range(d):
        for k in range(l):
            #机を使う時
            dp[i+1][j+1][k] += dp[i][j][k]
            #サバを使う時
            dp[i+1][j][k+1] += dp[i][j][k]
            #なにも使わない時
            dp[i+1][j][k] += dp[i][j][k]
print(dp)
print((ans * count) % mod)