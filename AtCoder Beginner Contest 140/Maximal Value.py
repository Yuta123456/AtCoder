n = int(input())
B = list(map(int, input().split()))
BMax = max(B) + 1
A = [BMax for i in range(n)]
for i in range(n - 1):
    A[i] = min(B[i], A[i])
    A[i + 1] = min(A[i + 1], B[i])
print(sum(A))
