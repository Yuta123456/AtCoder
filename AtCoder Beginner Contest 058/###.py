n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
mod = 10**9+7
#preprocess
#y_culculate
y_sum = 0
ans = 0
x_sum = 0
for i in range(1,m):
    h = y[i] - y[i-1]
    y_sum += h * i * (m - i)
    y_sum %= mod
for i in range(1,n):
    w = x[i] - x[i-1]
    x_sum += w * i * (n - i)
    x_sum %= mod
print((x_sum * y_sum) % mod)
    