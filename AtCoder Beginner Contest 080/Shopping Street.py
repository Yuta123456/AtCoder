import itertools 

n = int(input())
#shopの営業データ
shopData = []
#得点ドンぐらいとれるか
point = []
for i in range(n):
    shopData.append(list(map(int, input().split())))
for i in range(n):
    point.append(list(map(int, input().split())))
#最大値
data = itertools.product(range(2), repeat = 10)

max_point = - (10 ** 7)
def calcMax(data):
    global max_point
    earnPoint = 0
    for i in range(2 ** 10):
        if 1 in data[i]:
            for i in range(n):
                count = 0
                for j in range(10):
                    if shopData[i][j] == data[j] and data[j] == 1:
                         count += 1
                earnPoint += point[i][count]
        else:
            return
        if earnPoint > max_point:
            max_point = earnPoint
start = [None] * 10
print(max_point)