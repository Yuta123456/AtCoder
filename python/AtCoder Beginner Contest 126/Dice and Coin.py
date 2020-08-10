n, k = list(map(int, input().split()))
sum = 0
for i in range(1,n + 1):
    p = 1/n
    temp = i
    while temp < k:
        temp *= 2
        p /= 2
    sum += p
print(sum)
