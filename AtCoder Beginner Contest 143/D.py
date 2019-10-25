import bisect
n = int(input())
L = list(map(int, input().split()))
L.sort()
ans = 0
for i in range(n - 1, 0, -1):
    for j in range(i - 1, 0, -1):
        ans += max(0, (j - bisect.bisect_right(L, L[i] - L[j])))
print(ans)
