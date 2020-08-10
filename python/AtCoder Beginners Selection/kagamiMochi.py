num = int(input())
r = []
for i in range(num):
    r.append(int(input()))
r.sort()
count = 1
for i in range(num - 1):
    if r[i] < r[i + 1]:
        count = count + 1

print(count)
