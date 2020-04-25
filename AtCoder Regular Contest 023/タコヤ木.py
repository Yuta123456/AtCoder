import math
n = int(input())
a = list(map(int, input().split()))
memo = dict()
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
    if n in memo:
        return memo[n]
    else:
        
    return 
def mod_combination(n,k,mod):
    return mod_factorial(n,mod) * mod_inv(mod_factorial(k,mod), mod) * mod_inv(mod_factorial(n-k,mod), mod)
ans = 0
mod = 10**9+7
start_num = -1
end_num = -1
i = 0
while i < n:
    if a[i] == -1:
        count = 0
        start_num = a[i-1]
        while a[i] == -1:
            count += 1
            i += 1
        last_num = a[i]
        num_count = last_num - start_num + 1
        if num_count == 1:
            continue
        ans += mod_combination(num_count + count - 1, count, mod)
        ans %= mod
    else:
        i += 1
print(ans % mod)