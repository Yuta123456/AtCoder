a2b , b2c, c2a = map(int,input().split())
if b2c <= a2b and c2a <= a2b:
    print(b2c + c2a)
if a2b < b2c and  c2a <= b2c:
    print(a2b + c2a)
if b2c < c2a and a2b < c2a:
    print(b2c + a2b)
