n, m = map(int, input().split())
sum_value = 0
imos = [0 for i in range(m+2)]
for i in range(n):
    l, r, s = map(int, input().split())
    imos[l] += s
    imos[r+1] -= s
    sum_value += s
for i in range(m):
    imos[i+1] += imos[i]
print(sum_value - min(imos[1:-1]))