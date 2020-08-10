n = int(input())
c = list(input())
red_count = c.count('R')
ans = 0
for i in range(red_count):
    if c[i] == 'W':
        ans += 1
print(ans)