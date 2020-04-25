n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
dif = dict()
data.sort()
for i in range(n):
    for j in range(i+1, n):
        x = data[i][0] - data[j][0]
        y = data[i][1] - data[j][1]
        if (x,y) in dif:
            dif[(x,y)] += 1
        else:
            dif[(x,y)] = 1
if len(dif.keys()) == 0:
    print(n)
    exit()
print(n - max([dif[i] for i in dif.keys()]))
        
        

