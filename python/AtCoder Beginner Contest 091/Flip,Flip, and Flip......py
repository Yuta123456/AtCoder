n, m = list(map(int, input().split()))
#隣接するマスの個数が偶数であれば終わったときに裏を向いている
if n == 1 and m == 1:
    print(1)
elif n == 1:
    print(m - 2)
elif m == 1:
    print(n - 2)
else:
    k = m * 2 + n * 2 - 4
    print(m * n - k)
