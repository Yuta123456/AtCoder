a,r,n = map(int, input().split())
if r == 1:
    print(a)
else:
    n -= 1
    while n > 0:
        a *= r
        n -= 1
        if a > 10**9:
            print("large")
            exit()
    print(a)