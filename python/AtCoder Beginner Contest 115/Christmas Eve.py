n , k = list(map(int, input().split()))
h = []
for i in range(n):
    h.append(int(input()))
h.sort()
min = h[-1]
for i in range(n - k + 1):
    if min > h[i + k - 1] - h[i]:
        min = h[i + k - 1] - h[i]
print(min)
