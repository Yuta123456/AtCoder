n = int(input())
a = list(map(int, input().split()))
ans = 0
num = 1
index = 0
while index < n:
    if a[index] != num:
        ans += 1
    else:
        num += 1
    index += 1
if ans == n:
    print(-1)
else:
    print(ans)