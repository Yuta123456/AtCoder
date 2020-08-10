n, c = map(int, input().split())
data = [[0 for i in range(c+1)] for j in range(10**5+2)]
for i in range(n):
    s, t, channel = map(int, input().split())
    data[s][channel] += 1
    data[t+1][channel] -= 1
for i in range(c+1):
    for j in range(1,10**5+2):
        data[j][i] += data[j-1][i]
ans = 0
for i in range(10**5+2):
    sum_channel = 0
    for j in range(c+1):
        if data[i][j] == 1:
            sum_channel += 1
    ans = max(ans, sum_channel)
print(ans) 
