import copy
n, m = list(map(int, input().split()))
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())
#check
#何行目かを決める
for i in range(n + 1 - m):
    #何文字目かを決める
    for j in range(n + 1 - m):
        k = 0
        while 1:
            if a[i + k][j:j+m] != b[k]:
                break
            else:
                if k == m - 1:
                    print("Yes")
                    exit()
                k += 1
print("No")