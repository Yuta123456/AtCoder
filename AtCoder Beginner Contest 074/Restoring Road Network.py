n = int(input())
a = []
ans = 0
for i in range(n):
    k = list(map(int, input().split()))
    a.append(k)
flag = [[True for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[j][i] + a[i][k] < a[j][k]:
                print(-1)
                exit()
            elif a[j][i] + a[i][k] == a[j][k] and j != i and i != k:
                flag[j][k] = flag[k][j] = False
for i in range(n):
    for j in range(n):
        if flag[i][j]:
            ans += a[i][j]
print(ans//2)
