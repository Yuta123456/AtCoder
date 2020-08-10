import math
n = int(input())
min_len = 15
for i in range(1, int(math.sqrt(n)+1)):
    if n % i == 0:
        k = list(map(str, [n//i, i]))
        min_len = min(min_len, len(max(k, key = lambda x:len(x))))
print(min_len)
