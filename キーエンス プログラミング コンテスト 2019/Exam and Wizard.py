n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if sum(a) < sum(b):
    print(-1)
    exit()
else:
    sub = []
    sub = [0 for i in range(n)]
    for i in range(n):
        sub[i] = a[i] - b[i]
    ans = 0
    sub.sort()
    pool = 0
    index = 0
    k = -1
    while sub[index] < 0:
        ans += 1
        while sub[index] + pool < 0:
            pool += sub[k]
            sub[k] = 0
            k -= 1
            ans += 1
        pool += sub[index]
        index += 1
print(ans)

