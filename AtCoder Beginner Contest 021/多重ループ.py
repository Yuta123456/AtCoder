n = int(input())
k = int(input())
mod = 10**9 + 7
#初めに、nCkを考える
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
def mod_factorial(n,mod):
    ans = 1
    while n >= 2:
        ans  = (ans * n) % mod
        n -= 1
    return ans
def mod_combination(n,k,mod):
    return mod_factorial(n,mod) * mod_inv(mod_factorial(k,mod), mod) * mod_inv(mod_factorial(n-k,mod), mod)
ans = mod_combination(n+k-1,n-1,mod)
ans %= mod
print(ans)
