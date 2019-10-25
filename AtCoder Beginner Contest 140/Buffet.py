n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
total = 0
pre = n + 2
for i in range(n):
    total += B[A[i] - 1]
    if pre + 1 == A[i] - 1:
        total += C[pre]
    pre = A[i] - 1
print(total)
