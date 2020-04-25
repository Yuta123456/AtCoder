n,k,m,r = map(int, input().split())
s = []
for i in range(n-1):
    s.append(int(input()))
s.sort(reverse=True)
up_k = s[:k]
if sum(up_k) / k >= r:
    print(0)
else:
    up_k = s[:k-1]
    nes = (r * k) - sum(up_k)
    if nes <= m:
        print(nes)
    else:
        print(-1)
