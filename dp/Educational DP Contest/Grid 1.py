h, w = list(map(int, input().split()))
data = []
for i in range(h):
    data.append(list(input()))
dp = [[-1 for i in range(w)] for j in range(h)]
dp[0][0] = 1
def cal(row, column):
    if row < 0 or column < 0:
        return 0

    if data[row][column] == '#':
        return 0

    if dp[row][column] == -1:
        dp[row][column]  = cal(row - 1, column) + cal(row, column - 1)


    return dp[row][column]
mod = (10 ** 9) + 7
print(cal(h - 1, w - 1) % mod)
