n = int(input())
a = [0 for i in range(n)]
for i in range(n):
    a[i] = int(input())
a.sort()
ans = 0
if n == 2:
    print(a[1] - a[0])
if n % 2 == 1:
    ans += (a[-1] - a[0]) + (a[-2] - a[0])
    l = a[-1]
    r = a[-2]
    
else: