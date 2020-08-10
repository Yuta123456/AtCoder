import copy
n = int(input())
q = input()
a = ["." for i in range(n)]
def CalcAns():
    global a
    if calcTrue(q[0], a[0]):
        a[-1] = a[1]
    else:
        if a[1] == "W":
            a[-1] = "S"
        else:
            a[-1] = "W"
    print(a)
    check = copy.deepcopy(a[-1])
    for i in range(1,n-1):
        if calcTrue(q[i], a[i]):
            a[i - 1] = a[i + 1]
        else:
            if a[i + 1] == "W":
                a[i - 1] = "S"
            else:
                a[i - 1] = "W"
    if check == a[-1]:
        return True
    else:
        return False
    #data[0]の処理
def calcTrue(mark, kind):
    if kind == "S":
        if 'o' == mark:
            return True
        else:
            return False
    else:
        if  'o' != mark:
            return True
        else:
            return False
a[0] = "S"
a[1] = "S"
print(a)
if CalcAns():
    print(a)
    exit()
a[0] = "S"
a[1] = "W"
if CalcAns():
    print(a)
    exit()
a[0] = "W"
a[1] = "S"
if CalcAns():
    print(a)
    exit()
a[0] = "W"
a[1] = "W"
if CalcAns():
    print(a)
    exit()
print(-1)