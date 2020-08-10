import sys
input = sys.stdin.readline
h, w = map(int, input().split())
grid = []
bias_inf = 2000
for i in range(h):
    k = list(map(int, input().split()))
    grid.append(k)
for i in range(h):
    k = list(map(int, input().split()))
    for j in range(w):
        grid[i][j] = abs(grid[i][j] - k[j])

dp = [[[0 for i in range(-bias_inf,bias_inf)] for j in range(w)] for k in range(h)]
dp[0][0][0 - grid[0][0]] = 1
dp[0][0][0 + grid[0][0]] = 1
for i in range(h):
    for j in range(w):
        for k in range(-bias_inf,bias_inf):
            if i == h-1 and j == w-1:
                break
            if dp[i][j][k]:
                if i != h-1 and j != w-1:
                    dp[i][j+1][k + grid[i][j+1]] = 1
                    dp[i+1][j][k + grid[i+1][j]] = 1
                    dp[i][j+1][k - grid[i][j+1]] = 1
                    dp[i+1][j][k - grid[i+1][j]] = 1
                elif j == w-1:
                    dp[i+1][j][k - grid[i+1][j]] = 1
                    dp[i+1][j][k + grid[i+1][j]] = 1
                else:
                    dp[i][j+1][k - grid[i][j+1]] = 1
                    dp[i][j+1][k + grid[i][j+1]] = 1
ans = bias_inf
for i in range(-bias_inf,bias_inf):
    if dp[-1][-1][i]:
        ans = min(ans, abs(i))
print(ans)
