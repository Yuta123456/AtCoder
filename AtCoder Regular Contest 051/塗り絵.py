x_1, y_1, r = map(int, input().split())
x_2, y_2, x_3, y_3 = map(int, input().split())
def check(x,y):
    dis = (x - x_1)**2 + (y - y_1)**2
    dis = dis
    if dis <= r**2:
        return True
    else:
        return False
if x_2 <= x_1 - r and x_1 + r <= x_3 and y_2 <= y_1 - r and y_1 + r <= y_3:
    print("NO")
    print("YES")
elif check(x_2, y_2) and check(x_2, y_3) and check(x_3, y_2) and check(x_3, y_3) :
    print("YES")
    print("NO")
else:
    print("YES")
    print("YES")