import itertools
import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
acc = list(itertools.accumulate(a))
ans = 0
for i in range(n):
    index = bisect.bisect_right(a, acc[i]* 2)
    #print("index > {} i > {}  value > {}".format(index, i, acc[i] * 2))
    if index <= i + 1 and index < n:
        ans = i+1
print(n - ans)