n,k = map(int, input().split())
s = []
flag = False
for i in range(n):
    s.append(int(input()))
    if s[i] == 0:
        flag = True
if flag:
    print(n)
    exit()
#尺取り法をがんばってじっそうする。 ?
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
print(ans)