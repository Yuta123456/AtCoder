n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
min_value = sum(abs(i) for i in a)
total = 0
for i in range(n-1):
    total += a[i]
    if abs((2 * total) - sum_a) < min_value:
        min_value = abs((2 * total) - sum_a)
print(min_value)