n, m = map(int, input().split())
adjacent_list = [[] for i in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    adjacent_list[x].append(y)
dp = [-1 for i in range(n+1)]
def cul(x):
    if dp[x] != -1:
        return dp[x]
    else:
        if len(adjacent_list[x]) == 0:
            return 0
        dp[x] = max([cul(i) + 1 for i in adjacent_list[x]])
        return dp[x]
for i in range(1,n+1):
    cul(i)
print(max(dp))