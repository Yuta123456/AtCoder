n, k = list(map(int, input().split()))
count = 0
#when k <= i < j,  i % j >= k
if k == 0:
    print(n ** 2)
    exit()
for i in range(1, n + 1):
    if i <= k:
        continue
    count += max(0, (n % i) - k + 1)
    count += (n // i) * (i - k)
print(count)
