n = int(input())
a = list(map(int, input().split()))
k = list(range(1,n+1))
data = []
for i in range(n):
    data.append([a[i], k[i]])
data.sort(key=lambda x:x[0], reverse=True)
for i in range(n):
    print(data[i][1])
