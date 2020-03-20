
x, y = map(int, input().split())
#絶対値を一致させなければいけない
#かかるコストは、絶対値の差。+0 or+1 or +2
#ここは頑張って考える
if x == 0:
    if y >= 0:
        print(y)
    else:
        print(abs(y) + 1)
    exit()
elif y == 0:
    if x >= 0:
        print(1 + abs(x))
    else:
        print(abs(x))
    exit()
if y > 0 and x > 0:
    if y >= x:
        print(y - x)
    else:
        print(abs(x) - abs(y) + 2)
elif y < 0 and x > 0:
    if abs(y) > abs(x):
        print(abs(y) - x + 1)
    else:
        print(x - abs(y) + 1)
elif y > 0 and x < 0:
    if abs(x) < abs(y):
        print(y - abs(x) + 1)
    else:
        print(abs(x) - y + 1)
else:
    if y >= x:
        print(y - x)
    else:
        print(abs(y) - abs(x) + 2)


