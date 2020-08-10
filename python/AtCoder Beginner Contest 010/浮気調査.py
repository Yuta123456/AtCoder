import math
prex, prey, aftx, afty, T, V = list(map(int, input().split()))
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    dis1 = math.sqrt((prex - x)**2 + (prey - y)**2)
    dis2 = math.sqrt((aftx - x)**2 + (afty - y)**2)
    if (dis1 + dis2) / V <= T:
        print("YES")
        exit()
print("NO")