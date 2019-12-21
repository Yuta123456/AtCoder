x1,y1,x2,y2 = map(int, input().split())
n = int(input())
ans = 0
prex, prey = map(int, input().split())
s1,s2 = prex,prey
def intersect(p1, p2, p3, p4):
    tc1 = (p1[0] - p2[0]) * (p3[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p3[0])
    tc2 = (p1[0] - p2[0]) * (p4[1] - p1[1]) + (p1[1] - p2[1]) * (p1[0] - p4[0])
    td1 = (p3[0] - p4[0]) * (p1[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p1[0])
    td2 = (p3[0] - p4[0]) * (p2[1] - p3[1]) + (p3[1] - p4[1]) * (p3[0] - p2[0])
    return tc1*tc2<0 and td1*td2<0
for i in range(n-1):
    x,y = map(int, input().split())
    if intersect([x1,y1],[x2,y2],[x,y],[prex,prey]):
        ans += 1
    prex, prey = x,y
if intersect([x1,y1],[x2,y2],[s1,s2],[prex,prey]):
    ans += 1
print((ans//2) + 1)
