n = int(input())
data = []
for i in range(n):
    x, y, h = map(int, input().split())
    data.append([x,y,h])
data.sort(reverse=True, key = lambda x:x[2])
for Cx in range(0,101):
    for Cy in range(0,101):
        height = data[0][2] + abs(Cx - data[0][0]) + abs(Cy - data[0][1])
        for i in range(1,n):
            if data[i][2] != max(height - abs(Cx - data[i][0]) - abs(Cy - data[i][1]), 0):
                break
            if i == n - 1:
                print("{} {} {}".format(Cx,Cy,height))
                exit()
