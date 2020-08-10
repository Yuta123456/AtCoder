N = int(input())
data = list(map(int,input().split()))
dataSum = sum(data)
min = 10000
for i in range(N):
    sumT = sum(data[0:i + 1])
    if abs(sumT * 2 - dataSum)  < min:
        min = abs(sumT * 2 - dataSum)
    else:
        print (min)
        break
