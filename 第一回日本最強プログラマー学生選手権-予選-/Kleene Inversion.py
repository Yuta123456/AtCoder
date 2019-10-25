n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
mod = (10 ** 9) + 7
C = 0
t = 0
for i in range(n):
    for j in range(n):
        if A[i] > A[j] and i < j:
            t += 1
        if A[i] > A[j]:
            C += 1
print((t * k + (C * k * (k - 1) // 2)) % mod)
