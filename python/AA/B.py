a,v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
if a < b:
    if a + v * t >= b + w * t :
        print("YES")
    else:
        print("NO")
else : 
    if a - v * t <= b - w * t :
        print("YES")
    else:
        print("NO")