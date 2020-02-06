w, h = map(int, input().split())
mod = 7 + 10**9
def mod_factorial(n):
    ans = 1
    while n >= 2:
        ans  = (ans * n) % mod
        n -= 1
    return ans
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
h -= 1
w -= 1
k = h + w
k = mod_factorial(k)
h = mod_factorial(h)
w = mod_factorial(w)
print((k * mod_inv(h,mod) * mod_inv(w,mod) ) % mod)