n, k = map(int, input().split())
r = list(map(int, input().split()))
r.sort()
r = r[-k:]
ans = 0
for i in r:
    ans = (ans + i)/2
print(ans)
