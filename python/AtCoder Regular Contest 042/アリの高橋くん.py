x, y = map(int, input().split())
n = int(input())
prex, prey = map(int, input().split())
startx, starty = prex,prey
ans = 10**9
for i in range(n-1):
    cur_x, cur_y = map(int, input().split())
    a = prex - cur_x
    b = prey - cur_y 
    t = -( (a * (cur_x - x) + b * (cur_y - y))/ (a**2 + b**2))
    if t < 0:
        ans = min(ans, (cur_x - x)**2 + (cur_y - y) ** 2)
    elif t > 1:
        ans = min(ans, (prex - x)**2 + (prey - y) ** 2)
    else:
        ans = min(ans,  ((a * (cur_y - y) - b * (cur_x - x))**2)/ (a**2 + b**2))
    prex, prey = cur_x, cur_y
cur_x, cur_y = startx,starty
a = prex - cur_x
b = prey - cur_y 
t = -( (a * (cur_x - x) + b * (cur_y - y))/ (a**2 + b**2))
if t < 0:
    ans = min(ans, (cur_x - x)**2 + (cur_y - y) ** 2)
elif t > 1:
    ans = min(ans, (prex - x)**2 + (prey - y) ** 2)
else:
    ans = min(ans,  ((a * (cur_y - y) - b * (cur_x - x))**2)/ (a**2 + b**2))
print(ans**0.5)