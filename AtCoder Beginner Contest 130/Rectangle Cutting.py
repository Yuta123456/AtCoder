w, h, x, y = list(map(float,input().split()))
if w/2 == x and h/2 == y:
    print(w * h / 2.0, 1)
else:
    print(w * h / 2.0, 0)
