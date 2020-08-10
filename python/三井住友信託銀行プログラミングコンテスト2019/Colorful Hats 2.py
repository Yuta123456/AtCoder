n = int(input())
a = list(map(int, input().split()))
data = [[0]*3 for i in range(n+1)]
mod = 10**9+7
#data[i][0] => max: data[i][1] =>  middle: data[i][2] => min:
ans = 1
for i in range(n):
    tmp = data[i]
    ans *= tmp.count(a[i])
    ans %= mod
    for j in range(3):
        data[i+1][j] = data[i][j]
    for j in range(3):
        if data[i][j] == a[i]:
            data[i+1][j] += 1
            break
print(ans)