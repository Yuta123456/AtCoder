n, k, s = map(int, input().split())
ans = [0 for i in range(n)]
inf = 10**9
if s == inf:
    inf = 1
for i in range(n):
    if i < k:
        ans[i] = s
    else:
        ans[i] = inf
for i in range(n):
    print("{} ".format(ans[i]),end = "")
