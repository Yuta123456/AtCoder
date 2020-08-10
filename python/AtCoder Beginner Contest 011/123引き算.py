n = int(input())
ng = []
for i in range(3):
    ng.append(int(input()))
ng = set(ng)
dp  = [[False, 101] for i in range(n + 1)]
dp[-1][0] = True
dp[-1][1] = 0
if n in ng:
    print("NO")
    exit()
for i in range(n,-1,-1):
    if dp[i][0] and dp[i][1] < 100:
        for j in range(1,4):
            if i - j not in ng and i - j >= 0:
                dp[i-j][0] = True
                dp[i-j][1] = min(dp[i-j][1], dp[i][1] + 1)
if dp[0][0] and dp[0][1]<= 100:
    print("YES")
else:
    print("NO")