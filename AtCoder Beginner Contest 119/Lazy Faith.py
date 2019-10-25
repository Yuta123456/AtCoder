a,b,q = list(map(int, input().split()))
s = []
t = []
x = []
for i in range(a):
    s.append(int(input()))
for i in range(b):
    t.append(int(input()))
for i in range(q):
    x.append(int(input()))
def bisec(y,z,target,array):
    print("{} {} {} {}".format(y,z,target,array))
    if z == y + 1:
        if abs(array[y] - target) > abs(array[z] - target):
            return z
        else:
            return y
    elif array[int((y + z) / 2)] < target:
        bisec(int((y + z) / 2), z,target,array)
    else:
        bisec(y, int((y + z) / 2),target,array)
print(bisec(0,a,150,s))
