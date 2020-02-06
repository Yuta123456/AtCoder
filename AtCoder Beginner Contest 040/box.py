n = int(input())
ans = n+5
for i in range(1,n+1):
    h = i
    w = n//i
    q = n - (h * w)
    ans = min(ans, abs(h - w) + q)
print(ans)