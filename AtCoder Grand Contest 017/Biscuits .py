import math
n, p = map(int, input().split())
a = list(map(int, input().split()))
def combi(x, y):
    if y == 0:
        return 1
    if x == 0:
        return 0
    return math.factorial(x) / (math.factorial(x - y) * math.factorial(y))
odd_count = 0
even_count = 0
for i in range(n):
    if a[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
ans = 0
if p % 2 == 0:
    ans += 2 ** even_count
    ans += combi(odd_count, 2)
else:
    ans
    ans += combi(odd_count,2)
print(int(ans))
