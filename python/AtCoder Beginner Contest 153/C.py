n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
ans = 0
for i in range(min(k, len(h))):
    h[i] = 0
print(sum(h))
