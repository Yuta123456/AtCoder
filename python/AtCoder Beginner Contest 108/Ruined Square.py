x1, x2, y1, y2 = map(int, input().split())
x = y1 - x1
y = y2 - x2
print("{} {} {} {}".format(y1 - y , y2 + x , x1 - y , x2 + x))