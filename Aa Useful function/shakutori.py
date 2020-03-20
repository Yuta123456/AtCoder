left = 0
cur = 0
ans = 0
for right in range(n):
    cur += a[right]
    while cur > n:
        cur -= a[left]
        left += 1
    if cur == n:
        ans += 1