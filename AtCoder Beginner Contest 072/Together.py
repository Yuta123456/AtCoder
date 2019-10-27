import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
max = 0
for i in range((10 ** 5 ) + 1):
    cand = bisect.bisect_left(a, i + 3) - bisect.bisect_left(a, i)
    if max < cand:
        max = cand
print(max)