n = int(input())
memo = [0 for i in range(n)]
if n == 1:
    print(0)
    exit()
elif n == 2:
    print(0)
    exit()
elif n == 3:
    print(1)
    exit()
memo[2] = 1
memo[1] = 0
memo[0] = 0 
mod = 7 + 10**4
for i in range(3,n):
    memo[i] = (memo[i - 1] + memo[i - 2] + memo[i - 3]) % mod
print(memo[n - 1] % mod)