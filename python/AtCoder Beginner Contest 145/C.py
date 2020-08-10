import itertools
import math
n = int(input())
ans = 0
data = []
per = itertools.permutations(range(n))
for i in range(n):
    data.append(list(map(int, input().split())))
for i in per:
    for k in range(n):
        if  k == n - 1:
            break
        ans += math.sqrt(((data[i[k]][0] - data[i[k+1]][0]) ** 2) + ((data[i[k]][1] - data[i[k+1]][1]) ** 2))
print(ans / math.factorial(n))