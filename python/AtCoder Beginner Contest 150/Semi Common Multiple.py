import fractions
n, m = map(int, input().split())
a = [i//2 for i in list(map(int, input().split()))]
tmp = a[0]
count = 0
while tmp % 2 == 0:
    tmp /= 2
    count += 1
for i in range(n):
    tmp = a[i]
    div = 0
    while tmp % 2 == 0:
        tmp /= 2
        div += 1
    if div != count:
        print(0)
        exit()
ans = 0
k = a[0]
for i in range(n):
    k = (k * a[i]) // (fractions.gcd(k, a[i]))
ans = m // k
ans = (ans + 1) // 2
print(ans)