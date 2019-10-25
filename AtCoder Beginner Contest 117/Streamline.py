n , m = list(map(int, input().split()))
x = list(map(int, input().split()))
if n >= m:
    print(0)
    exit()
x.sort()
L = []
for i in range(m - 1):
    L.append(x[i + 1] - x[i])
L.sort()
L.reverse()
total = 0
for i in range(n - 1):
    total += L[i]
print(x[-1] - x[0] - total)
