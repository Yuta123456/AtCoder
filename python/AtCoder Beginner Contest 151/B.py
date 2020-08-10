n, k, m = map(int, input().split())
a = list(map(int, input().split()))
ans = sum(a)
for i in range(0,k+1):
    p = (ans + i)/n
    if p >= m:
        print(i)
        exit()
print(-1)