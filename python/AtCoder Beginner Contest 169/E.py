import bisect
n = int(input())
a = []
b = []

for i in range(n):
    m, p = map(int, input().split())
    a.append(m)
    b.append(p)
a.sort()
b.sort()
middle = n // 2
if n % 2:
    print(b[middle] - a[middle] + 1)
else: 
    a_m = ( a[middle] + a[middle - 1] ) / 2
    b_m = ( b[middle] + b[middle - 1] ) / 2
    print(int((b_m - a_m) * 2 + 1))




