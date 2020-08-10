def checkGo(x,y,t):
    if abs(x) + abs(y) > t or (t - (abs(x) + abs(y)) ) % 2 == 1:
        return False
    return True
count = int(input())
data = []
for i in range(count):
    data.append(list(map(int,input().split())))
passTime = 0
beforeX = 0
beforeY = 0
for i in data:
    time = i[0]
    x = i[1]
    y = i[2]
    if not checkGo(x - beforeX, y - beforeY, time - passTime):
        print("No")
        exit()
    passTime = i[0]
    beforeX = i[1]
    beforeY = i[2]
print("Yes")
