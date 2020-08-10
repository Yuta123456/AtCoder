x, y ,w = input().split(" ")
x = int(x)
y = int(y)
x -= 1
y -= 1
num = []
for i in range(9):
    num.append(list(map(int, list(input()))))
ans = ""
def check(s,t):
    if (0 <= s <= 8) and (0 <= t <= 8):
        return True
    else:
        return False
count = 0
if w == 'R':
    dx = 1
    dy = 1
    ans += str(num[y][x])
    while count < 3:
        if check(y,x + dx):
            ans += str(num[y][x+dx])
            x += dx
        else:
            dx *= -1
            ans += str(num[y][x+dx])
            x += dx
        count += 1
elif w == 'L':
    dx = -1
    dy = 1
    ans += str(num[y][x])
    while count < 3:
        if check(y,x + dx):
            ans += str(num[y][x+dx])
            x += dx
        else:
            dx *= -1
            ans += str(num[y][x+dx])
            x += dx
        count += 1
elif w == 'U':
    dx = 1
    dy = -1
    ans += str(num[y][x])
    while count < 3:
        if check(y + dy,x):
            ans += str(num[y+dy][x])
            y += dy
        else:
            dy *= -1
            ans += str(num[y+dy][x])
            y += dy
        count += 1
elif w == 'D':
    dx = 1
    dy = 1
    ans += str(num[y][x])
    while count < 3:
        if check(y + dy,x):
            ans += str(num[y+dy][x])
            y += dy
        else:
            dy *= -1
            ans += str(num[y+dy][x])
            y += dy
        count += 1
elif w == 'RU':
    dx = 1
    dy = -1
    ans += str(num[y][x])
    while count < 3:
        if check(y + dy,x + dx):
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        else:
            if not 0 <= y + dy <= 8:
                dy *= -1
            if not 0 <= x + dx <= 8:
                dx *= -1
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        count += 1
elif w == 'RD':
    dx = 1
    dy = 1
    ans += str(num[y][x])
    while count < 3:
        if check(y + dy,x + dx):
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        else:
            if not 0 <= y + dy <= 8:
                dy *= -1
            if not 0 <= x + dx <= 8:
                dx *= -1
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        count += 1
elif w == 'LU':
    dx = -1
    dy = -1
    ans += str(num[y][x])
    while count < 3:
        if check(y + dy,x + dx):
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        else:
            if not 0 <= y + dy <= 8:
                dy *= -1
            if not 0 <= x + dx <= 8:
                dx *= -1
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        count += 1
elif w == 'LD':
    dx = -1
    dy = 1
    ans += str(num[y][x])
    while count < 3:
        if check(y + dy,x + dx):
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        else:
            if not 0 <= y + dy <= 8:
                dy *= -1
            if not 0 <= x + dx <= 8:
                dx *= -1
            ans += str(num[y+dy][x+dx])
            y += dy
            x += dx
        count += 1
print(ans)
"""
8 8 R
790319030
091076399
143245946
590051196
398226115
442567154
112705290
716433235
221041645
"""