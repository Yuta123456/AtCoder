import math

n, m = list(map(int, input().split()))
reg = (m / n)
k = 1
for i in range(1, int(math.sqrt(m) + 1)):
    if m % i == 0:
        a = m/i
        b = i
        if reg >= b and k < b:
            k = b
        if reg >= a and k < a:
            k = a
print(int(k))
