n = int(input())
a = list(map(int, input().split()))
ans = pow(3, n)
if n == 1:
    if a[0] % 2 == 0:
        print(1)
    else:
        print(2)
else:
    num = 1
    for i in range(n):
        if a[i] % 2 == 0:
            num *= 2
        else:
            num *= 1
    print(ans - num)