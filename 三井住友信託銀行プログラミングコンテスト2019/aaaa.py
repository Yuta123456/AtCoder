t1, t2 = map(int, input().split())
a1,a2 = map(int, input().split())
b1, b2 = map(int, input().split())
#t1で生まれる差
P = (a1 - b1) * t1
#t2で生まれる差
Q = (a2 - b2) * t2
#P < 0 のことを仮定する
if P > 0:
    P *= -1
    Q *= -1

if P + Q < 0:
    print(0)
elif P + Q == 0:
    print("infinity")
else:
    #つぎのPを足したときに、負にいくかどうか？
    i = P * (-1)
    if i % (P + Q) == 0:
        print(2 * (i // (P + Q)))
    else:
        print(2 * (i // (P + Q)) + 1)
