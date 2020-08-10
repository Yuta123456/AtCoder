l,x,y,s,d = map(int, input().split())
#時計回りでの距離
if s > d:
    d += l
dis_1 = d - s
#半時計での距離
dis_2 = l - dis_1
if x >= y:
    print(dis_1 / (x + y))
else:
    print(min(dis_1 / (x + y), dis_2 / (y - x)))