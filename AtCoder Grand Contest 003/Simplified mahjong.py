n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
#適当な整数iを考えたとき、i-1の数字が余っているのであれば、それとペアを組ませるのが最適。
#余っていない時は、出来るだけ自分同士でペアを組む。もし一枚余るようであれば、残しておく
ans, a[0] = divmod(a[0], 2)
for i in range(1,n):
    pair = 0
    if a[i-1] > 0:
        pair = min(a[i-1], a[i])
        a[i-1] -= pair
        a[i] -= pair
    ans += pair
    pair, a[i] = divmod(a[i], 2)
    ans += pair
print(ans)