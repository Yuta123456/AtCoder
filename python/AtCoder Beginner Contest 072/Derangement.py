n = int(input())
p = list(map(int, input().split()))
count = 0
for i in range(n):
    if i == n - 1 and i + 1 == p[i]:
        count += 1
    elif i + 1 == p[i]:
        tmp = p[i]
        p[i] = p[i+1]
        p[i+1] = tmp
        count += 1
print(count)
