n, m = list(map(int, input().split()))
a = []
b = []
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.sort()
sum = 0
money = 0
index = 0
while sum + data[index][1]< m:
    sum += data[index][1]
    money += data[index][0] * data[index][1]
    del data[index]
money += (m - sum) * data[index][0]
print(money)
