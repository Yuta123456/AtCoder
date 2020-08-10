n = int(input())
ng = []
for i in range(3):
    ng.append(int(input()))

dp  = [101 for i in range(n + 1)]
dp[0] = 0
ng.sort()
for i in range(3):
    if n == ng[i]:
        print("NO")
        exit()
flag = False
if n == 2:
    for i in ng:
        if i == n - 1:
            flag = True
        else:
            flag = False
if n == 3:
    for i in ng:
        if i == n - 1:
            flag = True
        else:
            flag = False
if flag:
    print("NO")
    exit()
if ng[0] + 1 == ng[1] and ng[1] + 1 == ng[2]:
    print("NO")
    exit()

for i in range(n):
    if i == ng[0] or i == ng[1] or i == ng[2]:
        continue
    else:
        for j in range(1,4):
            if i + j > n:
                break
            dp[i + j] = min(dp[i] + 1, dp[i + j])

if dp[n] <= 100:
    print("YES")
else:
    print("NO")
