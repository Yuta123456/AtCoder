n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
mother_x = 0
child_x = 0
mother_y = 0
child_y = 0
for i in range(n):
    x,y,c = data[i]
    mother_x += c
    mother_y += c
    child_x += c*x
    child_y += c*y
ans_x = child_x / mother_x
ans_y = child_y / mother_y
print("x: {}, y: {}".format(ans_x,ans_y))
ans = 0
for i in range(n):
    x,y,c = data[i]
    ans = max(ans, c * max(abs(x-ans_x),  abs(y-ans_y)))
print(ans)

