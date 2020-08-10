from fractions import gcd
n, m = map(int, input().split())
s = input()
t = input()
#一文字目が違うと無理
gcd_n_m = gcd(n,m)
if gcd_n_m == 1 and s[0] == t[0]:
    print(n*m)
else:
    step_s = n // gcd_n_m
    step_t = m // gcd_n_m
    index_s = 0
    index_t = 0
    while index_s < n and index_t < m:
        if s[index_s] != t[index_t]:
            print(-1)
            exit()
        index_s += step_s
        index_t += step_t
    print(n*m//gcd_n_m)
