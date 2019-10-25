import math
def com(x, y):
    k = math.factorial(x)
    s = math.factorial(y)
    l = math.factorial(x - y)
    return k // (s * l)
n = int(input())
a = list(map(int, input().split()))
a.sort()
max = a[-1]
target = max / 2
min = a[0]
for i in range(n - 1):
    if abs(a[i] - target) < abs(min - target):
        min = a[i]
print("{} {}".format(max, min))
