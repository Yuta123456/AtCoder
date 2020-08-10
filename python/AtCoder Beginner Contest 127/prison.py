n, m = list(map(int, input().split()))
data = []
data1 = []
data2 = []
for i in range(m):
    data.append(list(map(int, input().split())))
for i in range(m):
    data1.append(data[i][0])
    data2.append(data[i][1])
if min(data2) - max(data1)  + 1 > 0:
    print(min(data2) - max(data1) + 1)
else:
    print(0)
