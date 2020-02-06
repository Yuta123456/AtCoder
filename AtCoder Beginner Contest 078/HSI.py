n, m = map(int, input().split())
x = 1900 * m + 100 * (n - m)
print(x * (2**m))