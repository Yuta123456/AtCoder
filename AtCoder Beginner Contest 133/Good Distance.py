import math
n, d =list(map(int, input().split()))
data = []
count = 0
sum = 0
for i in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    for j in range(i + 1, n):
        sum = 0
        for k in range(d):
            sum += (data[i][k] - data[j][k]) * (data[i][k] - data[j][k])
        if math.sqrt(sum).is_integer():
            count += 1
print(count)
