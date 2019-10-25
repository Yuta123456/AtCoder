n = int(input())
data = list(map(int, input().split()))
count = 0
for i in range(n):
    if data[i] < 0:
        count += 1
    data[i] = abs(data[i])
if count % 2 == 0:
    print(sum(data))
else:
    print(sum(data) - min(data) * 2)
