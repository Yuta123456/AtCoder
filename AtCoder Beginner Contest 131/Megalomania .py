from operator import itemgetter
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort(key = itemgetter(1))
time = 0
for i in range(n):
    time += data[i][0]
    if time > data[i][1]:
        print("No")
        exit()
print("Yes")
