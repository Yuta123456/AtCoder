import sys
n = int(input())
v = 0
max_di = 0
for i in range(2,n+1):
    print("? {} {}".format(1,i))
    sys.stdout.flush()
    inp = int(input())
    if max_di < inp:
        v = i
        max_di = inp
ans = 0
for i in range(1,n+1):
    if v == i:
        continue
    print("? {} {}".format(v,i))
    sys.stdout.flush()
    inp = int(input())
    if ans < inp:
        ans = inp
print("! {}".format(ans))