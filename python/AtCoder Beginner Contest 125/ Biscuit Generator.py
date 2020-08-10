a, b, t = list(map(int, input().split()))
i = 0
while (i * a) <= t:
    i += 1
print((i - 1) * b)
