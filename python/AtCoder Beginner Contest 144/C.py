import math
n = int(input())
min = n + 5
for i in range(1, 1 + int(math.sqrt(n))):
    if n % i == 0 and min > i + (n // i):
        min = i + (n // i)
print(min - 2)