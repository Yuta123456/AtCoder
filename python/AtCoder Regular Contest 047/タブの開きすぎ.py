n, l = map(int, input().split())
s = list(input())
now = 1
ans = 0
for i in range(n):
    if s[i] == '+':
        now += 1
    else:
        now -= 1
    if now > l:
        ans += 1
        now = 1
print(ans)