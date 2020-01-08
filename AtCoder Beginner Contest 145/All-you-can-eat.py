n, t = map(int, input().split())
food = []
for i in range(n):
    food.append(list(map(int, input().split())))
food.sort(key = lambda x:x[0])
b_max = [0 for i in range(n+2)]
for i in range(n):
    b_max[-(i+2)] = max(b_max[-(i+1)], food[-(i+1)][1])
dp = [[0 for i in range(t+1)] for j in range(n+1)]
for i in range(n):
    for j in range(t+1):
        if j + food[i][0] < t:
            dp[i+1][j + food[i][0]] = max(dp[i+1][j + food[i][0]], dp[i][j] + food[i][1])
        dp[i+1][j] = max(dp[i+1][j], dp[i][j])
ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][-2] + b_max[i+1])
print(ans)