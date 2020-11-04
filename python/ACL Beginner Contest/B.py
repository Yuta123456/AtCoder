a, b, c, d = map(int, input().split())
length = max(a,b,c,d) - min(a,b,c,d)
one = b - a
two = d - c
if length > one + two:
    print('No')
else:
    print('Yes')
