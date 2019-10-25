n, k = map(int, input().split())
h = list(map(int, input().split()))
sum = 0
for i in h:
    if i >= k:
        sum += 1
print(sum)
