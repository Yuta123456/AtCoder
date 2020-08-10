n = int(input())
a = list(map(int, input().split()))

data = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    data[i][0] = a[i]
    data[i][1] = i + 1
data.sort()
for i in range(n):
    print(data[i][1], end = " ")
