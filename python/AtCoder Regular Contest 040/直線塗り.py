n,r = map(int, input().split())
s = list(input())
ans = -1
last_empty = -1
for i in range(n):
    if s[i] == '.':
        last_empty = i
last_shot = last_empty - r + 1
if last_empty == -1:
    print(0)
    exit()
if last_shot <= 0:
    print(1)
    exit()
else:
    now = -1
    while now < last_shot - 1:
        now += 1
        ans += 1
        if s[now] == '.':
            ans += 1
            for j in range(now, min(now+r,n)):
                s[j] = 'o'
ans += 2
print(ans) 