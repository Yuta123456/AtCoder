n,m = map(int, input().split())
data = []
inf = 10**10
for i in range(m):
    data.append(input().split())
dp = [[inf for i in range(2**n)] for j in range(m+1)]
for i in range(m+1):
    dp[i][0] = 0
for i in range(1,m+1):
    s, c = data[i-1]
    c = int(c)
    bit = ""
    for j in s:
        if j == "Y":
            bit += "1"
        else:
            bit += "0"
    bit = int(bit,2)
    for j in range(2**n):
        next_i = int(str(j | bit))
        dp[i][next_i] = min(dp[i][next_i], dp[i-1][j] + c)
        dp[i][j] = min(dp[i][j], dp[i-1][j])
if dp[-1][-1] == inf:
    print(-1)
else:
    print(dp[-1][-1])
        
