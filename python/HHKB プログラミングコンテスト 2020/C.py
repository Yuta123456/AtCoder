n = int(input())
p = list(map(int, input().split()))
ans = 0
finished = set()
for i in range(n):
    finished.add(p[i])
    while ans in finished:
        ans += 1
    print(ans)