n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n):
    a[i] = a[i] - (i + 1)
if n == 1:
    print(0)
    exit()
a.sort()
if n % 2 == 0:
    ave = a[int(n/2)]
    for i in range(n):
        total += abs(a[i] - ave)
    print(total)
else:
    total2 = 0
    ave = a[int(n/2)]
    for i in range(n):
        total += abs(a[i] - ave)
    ave = a[int((n + 1)/2)]
    for i in range(n):
        total2 += abs(a[i] - ave)
    if total2 >= total:
        print(total)
    else:
        print(total2)
