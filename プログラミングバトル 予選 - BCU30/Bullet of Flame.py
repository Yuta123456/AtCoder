n , p = list(map(int, input().split()))
A = list(map(int, input().split()))
data = []
data.append(0)
for i in range(n):
    data.append(data[i] + A[i])
    if data[i + 1] > p:
        print(i)
        exit()
print(n)
