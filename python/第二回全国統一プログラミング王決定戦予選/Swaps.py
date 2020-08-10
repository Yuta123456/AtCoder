n, m = list(map(int, input().split()))
inf = 10.0 ** 10
path_data = []
for i in range(m):
    path_data.append(list(map(int, input().split())))
path_data.sort()
dp = [inf] * (n + 1)
dp[0] = 0
dp[1] = 0
for i in range(m):
    l = path_data[i][0]
    r = path_data[i][1]
    c = path_data[i][2]
    if dp[l] == inf:
        continue
    for j in range(l, r+1):
        dp[j] = min(dp[j], dp[l] + c)
if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])
