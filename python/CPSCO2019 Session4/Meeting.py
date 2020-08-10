import itertools
n,d = map(int, input().split())
s = []
for i in range(d):
    s.append(list(input()))
cand = itertools.combinations(range(d),2)
ans = 0
for day1, day2 in cand:
    attend = set()
    for i, mark in enumerate(s[day1]):
        if mark == 'o':
            attend.add(i)
    for i, mark in enumerate(s[day2]):
        if mark == 'o':
            attend.add(i)
    ans = max(ans, len(attend))
print(ans)
