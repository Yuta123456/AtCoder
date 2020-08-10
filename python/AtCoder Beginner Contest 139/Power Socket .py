a,b = map(int, input().split())
k = a - 1
count = 0
tap = 1
while tap < b:
    tap += k
    count += 1
print(count)
