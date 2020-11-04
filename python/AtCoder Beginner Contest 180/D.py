x, y, a, b = map(int, input().split())
ans = 0
while a * x < b and a * x < y:
    x = a * x
    ans += 1
if (y-x) % b == 0:
    count = (y - x) // b - 1
else:
    count = (y - x) // b
ans += count
print(ans)