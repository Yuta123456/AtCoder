n = int(input())
data = []
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    ans += (a + b) * (b - a + 1) // 2
print(ans)