import math
h  = int(input())
w  = int(input())
n  = int(input())
k = max(w, h)
print(math.ceil(n / k))