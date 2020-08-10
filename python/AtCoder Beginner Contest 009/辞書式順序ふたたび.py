import copy
from collections import Counter
n, k = map(int, input().split())
s = list(input())
s_sort = sorted(s)
t = ""
dif = 0
for i in range(n):
    for c in s_sort:
        # もし、t + c がok
        if s[i] == c:
            dif1 = dif
        else:
            dif1 = dif + 1
        pre = Counter(s[i+1:])
        unuse = Counter(s) - pre
