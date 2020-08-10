n = int(input())
s = list(input())
t = list(input())
count = 0
if s == t:
    print(n)
    exit()
for i in range(n):
    index = 0
    while s[i + index] == t[index]:
        index += 1
        if index + i == n:
            count = max(count, n - i)
            break

print(n * 2 - count)