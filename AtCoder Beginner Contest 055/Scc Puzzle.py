n, m = list(map(int, input().split()))
if n >= m:
    print(m//2)
else:
    m += n * 2
    print(m // 4)