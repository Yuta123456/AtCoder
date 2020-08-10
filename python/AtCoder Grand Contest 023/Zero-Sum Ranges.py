import itertools
n = int(input())
a = list(map(int, input().split()))
a = [0] + a
acc = list(itertools.accumulate(a))
pre = {}
ans = 0
for i in range(n+1):
    if acc[i] in pre:
        ans += pre[acc[i]]
        pre[acc[i]] += 1
    else:
        pre[acc[i]] = 1
print(ans)

