x = int(input())
ans = 1
for i in range(2, int(x**0.5) + 1):
    n = 2
    while i ** (n+1) <= x:
        n += 1
    ans = max(ans, i**n)
print(ans)