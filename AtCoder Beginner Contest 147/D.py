import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.reverse()
mod = 7 + 10**9
leng = 60
data = [[0 for i in range(leng+1)] for j in range(n)]
#pre
for i in range(n):
    k = list(bin(a[i]))
    k.reverse()
    ll = len(k)
    for j in range(1, leng+1):
        temp = data[i - 1][j]
        if j - 1 >= ll:
            data[i][j] = temp
            continue
        if k[j - 1] == "1":
            data[i][j] = temp + 1
        else:
            data[i][j] = temp
ans = 0
a.reverse()
data.reverse()
for i in range(n-1):
    k = format(a[i], 'b')
    k = list(k)
    k.reverse()
    k = k + [0 for s in range(leng - len(k))]
    for j in range(leng):
        if k[j] == "1":
            ans += ((n - i - 1) - data[i+1][j+1]) * (2**j)
            ans %= mod
        else:
            ans += data[i+1][j+1] * (2**j)
            ans %= mod
print(ans)
