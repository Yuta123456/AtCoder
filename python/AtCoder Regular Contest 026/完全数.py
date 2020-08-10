import math
n = int(input())
total = 1
if n == 1:
    print("Deficient")
    exit()
for i in range(2,int(n**0.5 + 1)):
    if n % i == 0:
        total += (i + (n // i))
        if i == n // i:
            total -= i
if total > n:
    print("Abundant")
elif total < n:
    print("Deficient")
else:
    print("Perfect")
