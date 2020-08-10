from collections import Counter
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a = Counter(a)
ans = 0
print(a)
for i in a:
    if a[i] % 2 == 1:
        ans += 1
print(ans)