n = int(input())
memo = [0 for i in range(10)]
memo[1] = 1
for i in range(2,10):
    memo[i] = memo[i-1] * 10 + 10**(i - 1)
print(memo)
leng = len(str(n)) - 1
ans = memo[leng]

