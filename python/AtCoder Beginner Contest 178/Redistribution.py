s = int(input())
mod = 10**9 + 7
ans = 0
fact = [1 for i in range(2*s+1)]
for i in range(1,2*s):
    fact[i+1] = fact[i] * (i+1) % mod
for i in range(s//3 ,s + 1):
    remain_ball = s - 3 * i
    #ans += fact[remain_ball + i-1] * pow(fact[remain_ball],-1,mod) * pow(fact[i-1],-1,mod)
    ans %= mod
print(ans)
print(fact)