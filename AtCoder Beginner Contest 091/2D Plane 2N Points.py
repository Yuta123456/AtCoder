n = int(input())
red = []
blue = []
for i in range(n):
    red.append(list(map(int, input().split())))
for i in range(n):
    blue.append(list(map(int, input().split())))
#xの昇順のソート
red.sort(key=lambda x:x[0])
blue.sort(key=lambda x:x[0])
ans = 0
delete_value = set([-1])
for b in range(n):
    maxY = -1
    for r in range(n):
        if blue[b][0] < red[r][0]:
            break
        else:
            if blue[b][1] > red[r][1] and red[r][1] not in delete_value:
                maxY = max(maxY, red[r][1])
    delete_value.add(maxY)
print(len(delete_value)-1)    

