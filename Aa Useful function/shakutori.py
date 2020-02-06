ans = 0
left = 0
right = 0
now = 1
while left < n:
    while right < n and now * s[right] <= k:
        now *= s[right]
        right += 1
        ans = max(ans, right - left)
    now  = now / s[left]
    left += 1
    if right <= left and right < n:
        now *= s[right]
        right += 1