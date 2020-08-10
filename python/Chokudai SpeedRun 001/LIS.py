import bisect
n = int(input())
a = list(map(int, input().split()))
inf = 10**9
dp = [inf for i in range(n)]
cur_max = 0
#dp[i] := i+1個増加部分列を作れた時の、一番最後の数字の最小値
for i in range(n):
    index = bisect.bisect_left(dp, a[i])
    dp[index] = a[i]
for i in range(n-1,-1,-1):
    if dp[i] != inf:
        print(i+1)
        exit()
