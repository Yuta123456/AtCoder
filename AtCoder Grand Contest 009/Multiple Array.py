n = int(input())
ans = 0
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.reverse()
for i in range(n):
    a, b = data[i]
    if (a + ans) % b != 0:
        ans += (b - ((a + ans) % b))
print(ans)

