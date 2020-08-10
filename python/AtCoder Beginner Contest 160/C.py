k,n = map(int, input().split())
a = list(map(int, input().split()))
ans = 10**9
for i in range(n-1):
    ans = min(ans, k - (a[i+1] - a[i]))
ans = min(ans, k - (a[0] + k - a[-1]))
print(ans)