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
data = list(itertools.product(range(2), repeat = 10))
del data[0]
max_point = - (10 ** 9)
for shop in data:
    cand = 0
    for i in range(len(shopData)):
        count = 0
        for j in range(10):
            if shop[j] == 1 and shopData[i][j] == 1:
                count += 1
        cand += point[i][count]
    max_point = max(max_point, cand)
print(max_point)
                
