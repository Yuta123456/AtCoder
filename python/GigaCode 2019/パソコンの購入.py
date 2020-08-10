import itertools
d = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
min_pc = 2000000001
a = list(itertools.accumulate(a))
for i in range(d):
    if a[i] >= b[i] and min_pc > b[i]:
        min_pc = b[i]
if min_pc == 2000000001:
    print(-1)
else:
    print(min_pc)