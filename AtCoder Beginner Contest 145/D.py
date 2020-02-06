import math
x,y = list(map(int, input().split()))
mod = 7 + (10**9)
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
if (2 * x - y) % 3 != 0 or (2 * y - x) % 3 != 0:
    print(0)
    exit()
else:
    m = (2*x - y)//3
    n = (2*y - x)//3
    if n < 0 or m < 0:
        print(0)
        exit()
    #m+n C m を計算
    #(m+n)! / n! * m!を計算したいが、mod上で割り算できない。
    #逆元を使う
    factorial = [1]*(m+n+1)
    for i in range(1,m+n+1):
        factorial[i] = (factorial[i - 1] * i) % mod
    ans = factorial[m+n] * mod_inv(factorial[m], mod)
    ans %= mod
    ans *= mod_inv(factorial[n], mod)
    ans %= mod
    print(ans)
