n,m,d = map(int, input().split())
a = list(map(int, input().split()))
#ダブリングをする
doubling = [[-1 for i in range(n+1)] for j in range(60)]
to = [i for i in range(n+1)]
for i in range(m):
    k = a[i]
    to[k], to[k+1] = to[k+1], to[k]
#to[i] := to[i]が最終的にはiに来る
for i in range(n):
    k = to[i+1]
    doubling[0][k] = i + 1
for i in range(1, 60):
    for j in range(1, n+1):
        tmp = doubling[i-1][j]
        doubling[i][j] = doubling[i-1][tmp]

for i in range(1, n+1):
    now = i
    remain = d
    for j in range(61):
        if (1 << j) & remain >= 1:
            now = doubling[j][now]
            remain -= (1 << j)
    print(now)




