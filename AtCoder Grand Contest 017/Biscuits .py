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
    ans += pow(2,even_count)
    tmp = 0
    for i in range(0,odd_count+1,2):
        tmp += combi(odd_count,i)
    ans *= tmp
else:
    ans += pow(2,even_count)
    tmp = 0
    for i in range(1,odd_count+1,2):
        tmp += combi(odd_count,i)
    ans *= tmp
print(int(ans))
