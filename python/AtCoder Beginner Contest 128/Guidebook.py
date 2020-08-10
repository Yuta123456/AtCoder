n = int(input())
data = []
for i in range(n):
    k = [i + 1] + list(input().split())
    data.append(k)
data = sorted(data, key = lambda x: (x[1], -int(x[2])))
for i in range(n):
    print(data[i][0])
