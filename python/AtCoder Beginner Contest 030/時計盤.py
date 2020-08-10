n,m = map(int, input().split())
n %= 12
n *= 5
n += m / 12
print(min(abs(n - m) * 6, 360 - abs(n - m) * 6))