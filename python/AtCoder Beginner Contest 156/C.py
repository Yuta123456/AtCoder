n = int(input())
x = list(map(int, input().split()))
ans = 10**8
for i in range(0,101):
    cand = 0
    for j in range(n):
        cand += (i - x[j]) ** 2
    ans = min(ans, cand)
print(ans)
