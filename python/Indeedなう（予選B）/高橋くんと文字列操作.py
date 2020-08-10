from collections import deque
s = list(input())
t = list(input())
s = deque(s)
t = deque(t)
ans = 0
if s == t:
    print(ans)
    exit()
for i in range(len(s)):
    ans += 1
    k = s.pop()
    s.appendleft(k)
    if s == t:
        print(ans )
        exit()
print(-1)