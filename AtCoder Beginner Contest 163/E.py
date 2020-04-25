import copy
n = int(input())
a = list(map(int, input().split()))
array = [(a[i], i+1) for i in range(n)]
array.sort(reverse=True)
dp = [[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n):
    for j in range(n):
        if i + j >= n:
            break
        count = i + j
        #右に移した場合
        value, index = array[count]
        dp[i][j+1] = max(dp[i][j+1], dp[i][j] + value * abs((n - j) - index))
        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + value * abs((i + 1) - index))
ans = 0
for i in range(n+1):
    for j in range(n+1):
        ans = max(ans, dp[i][j])
print(ans)
        


