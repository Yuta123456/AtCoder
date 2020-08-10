import math
a, b, x = list(map(int, input().split()))
capa = a * a * b
if capa / 2 < x:
    l = ( 2 * (capa - x) ) / (a*a)
    print(math.degrees(math.atan(l/a)))
    exit()
else:
    l = (2 * x) / (b * a)
    print(math.degrees(math.atan(b/l)))
    exit()