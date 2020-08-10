n, m = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.reverse()
while m > 0:
    A[0] = A[0] // 2
    m -= 1
    i = 1
    while m > 0 and i < n:
        if A[i] > A[0]:
            A[i] = A[i] // 2
            m -= 1
            i += 1
        else:
            break
    A.sort()
    A.reverse()
print(sum(A))
