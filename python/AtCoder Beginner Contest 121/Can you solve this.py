n, m, c = list(map(int ,input().split()))
b = list(map(int ,input().split()))
A = []
for i in range(n):
    A.append(list(map(int ,input().split())))
count = 0
for i in range(n):
    sum = 0
    for j in range(m):
        sum += (b[j] * A[i][j])
    if sum + c > 0:
        count += 1
print(count)
