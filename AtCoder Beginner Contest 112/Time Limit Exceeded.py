n, t = list(map(int, input().split()))
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
minCost = 1001
for i in range(n):
    if data[i][1] <= t and minCost > data[i][0]:
        minCost = data[i][0]

if minCost == 1001:
    print("TLE")
else:
    print(minCost)
