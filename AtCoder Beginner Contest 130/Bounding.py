n, x = list(map(int, input().split()))
L = list(map(int, input().split()))
length = 0
i = 0
count = 1
while n > i:
    length += L[i]
    if length <= x:
        count += 1
    i += 1
print(count)
