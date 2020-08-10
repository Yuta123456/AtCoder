import itertools
n, m = map(int, input().split())
a = list(map(int,input().split()))
acc = list(itertools.accumulate(a))
ans = 0
reminder = {}
reminder[0] = 0
for i in range(n):
    rem = acc[i] % m
    if rem == 0:
        reminder[rem] += 1
        ans += reminder[rem]
        continue
    if rem not in reminder:
        reminder[rem] = 1
    else:
        ans += reminder[rem]
        reminder[rem] += 1
print(ans)
