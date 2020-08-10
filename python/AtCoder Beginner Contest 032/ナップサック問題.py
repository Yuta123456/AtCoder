n, w = map(int, input().split())
data = []
flag = True
for i in range(n):
    data.append(list(map(int, input().split())))
    if not (1 <= data[0] <= 1000):
        flag = False

if n <= 30:
    a = []
    b = []
    for i in range(n):
        if i % 2 == 0:
            a.append(data[i])
        else:
            b.append(data[i])
    
elif flag:
    #dp[n][v]
else:
    #dp[n][w]