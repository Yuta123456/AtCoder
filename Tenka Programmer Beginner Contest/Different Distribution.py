n  =int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
ans = data[-1][0] - data[0][0] + 1
ans += data[0][0] - 1
ans += data[-1][1]
print(ans)