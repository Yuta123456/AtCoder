n = int(input())
a = list(map(int, input().split()))
ans = 1
a.sort()
for i in range(n):
    ans *= a[i]
    if ans > 10**18:
        print(-1)
        exit()
print(ans)