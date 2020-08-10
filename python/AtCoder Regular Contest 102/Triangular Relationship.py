n, k = list(map(int, input().split()))
count = 0
i = 1
zero = 0
rem = 0
if k % 2 == 0:
    while i <= n:
        if i % k == 0:
            zero += 1
        elif i % int(k/2) == 0:
            rem += 1
        i += 1
    print(zero ** 3 + rem ** 3)
else:
    while i <= n :
        if i % k == 0:
            count += 1
        i += 1
    print(count ** 3)
