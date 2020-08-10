import numpy as np
a, b = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
n = np.zeros((b + 1, a + 1))
n[0][0] = 0
for i in range(1,a + 1):
    if i % 2 == 0:
        n[0][i] = n[0][i - 1]
    else:
        n[0][i] = n[0][i - 1] + A[i - 1]
for i in range(1,b + 1):
    if i % 2 == 0:
        n[i][0] = n[i - 1][0]
    else:
        n[i][0] = n[i - 1][0] + B[i - 1]

for i in range(1,b + 1):
    for j in range(1,a + 1):
        if (i + j) % 2 == 0:
            n[i][j] = max(n[i - 1][j], n[i][j - 1])
            ##ここな気がする
        else:
            geta = n[i][j - 1] + A[j - 1]
            getb = n[i - 1][j] + B[i - 1]
            n[i][j] = max(geta,getb,n[i][j])
print(n)
print(int(np.amax(n)))
