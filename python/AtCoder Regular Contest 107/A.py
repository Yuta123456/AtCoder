a, b, c = map(int, input().split())
mod = 998244353
s_a = (a * (a+1)) // 2
s_b = (b * (b + 1)) // 2
s_c = (c * (c+1)) // 2
print(s_a * s_b * s_c % mod)
