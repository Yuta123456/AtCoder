import math
n,  h = map(int,input().split())
a,b,c,d,e = map(int, input().split())
ans = 10 ** 12
#普通の食事をする回数を固定
for x in range(n+1):
    #質素な食事をする回数が固定される

    y = max(math.ceil(((n * e) - (e * x) - (b * x) - h + 0.00001) / (d + e)), 0)
    #print("x:{} y:{} ans:{}".format(x,y,a*x+c*y))
    ans = min(ans, a * x + c * y)
print(ans)