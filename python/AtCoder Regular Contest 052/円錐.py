from math import pi
n, q = map(int, input().split())
area_accumulate = [0 for i in range(10**4+3)]
#area_accumulate[i] => i~(i+1)までの 
for _ in range(n):
    x, r, h = map(int, input().split())
    all_area = pi*r*r*h / 3
    sum_area = 0
    dr = r / h
    r -= dr
    for i in range(h):
        now_area = all_area - ((h - (1 + i))*r*r*pi/3) - (sum_area)
        area_accumulate[x+i] += now_area
        r -= dr
        sum_area += now_area
for i in range(1,len(area_accumulate)):
    area_accumulate[i] += area_accumulate[i-1]
area_accumulate[-1] = 0
for i in range(q):
    a,b = map(int, input().split())
    print(area_accumulate[b-1] - area_accumulate[a-1])
