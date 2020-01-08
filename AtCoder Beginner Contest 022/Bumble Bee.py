n = int(input())
a = set()
ans = 0
for i in range(n):
    k = int(input())
    if k in a:
        ans += 1
    else:
        a.add(k)

print(ans)