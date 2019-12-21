a,b,x = map(int, input().split())
if a % x != 0:
    a += x - (a%x)
if b % x != 0:
    b -= b%x
print(1 + (b - a) // x)