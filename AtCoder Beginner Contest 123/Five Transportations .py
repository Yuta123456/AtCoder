import math

n = int(input())
k = []
for i in range(5):
    k.append(int(input()))
print(math.ceil(n / min(k)) + 4)
