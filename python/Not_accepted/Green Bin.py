n = int(input())
b = [[] * 2 for i in range(n)]
a = ''
for i in range(n):
    a = input()
    a = sorted(a)
    if index

i = 0
j = 0
ans = 0
count = 1
while i < len(b):
    j = i + 1
    count = 1
    while j < len(b):
        if b[i] == b[j]:
            ans += count
            count += 1
            del b[j]
        j += 1
    i += 1
print(ans)
