def bisection_L_Method(a, b):
    while a + 1 < b:
        if checkleft(int((a + b) / 2)):
            a = int((a + b) / 2)
        else:
            b = int((a + b) / 2)
    return a

def bisection_R_Method(a, b):
    while a + 1 < b:
        if checkright(int((a + b) / 2)):
            b = int((a + b) / 2)
        else:
            a = int((a + b) / 2)
    return b

def checkleft(num):
    for i in range(q):
        if quel[i][0] == s[num]:
            if quel[i][1] == 'L':
                num -= 1
            else:
                num += 1
        if num < 0:
            return True
        elif num > n - 1:
            return False
    return False

def checkright(num):
    for i in range(q):
        if quel[i][0] == s[num]:
            if quel[i][1] == 'L':
                num -= 1
            else:
                num += 1
        if num > n - 1:
            return True
        elif num < 0:
            return False
    return False

n , q = list(map(int,input().split()))
s = input()
quel = []
data = []
count = 0
for i in range(q):
    quel.append(list(input().split()))
L0 = checkleft(0)
R0 = checkright(0)
Ln = checkleft(n - 1)
Rn = checkright(n - 1)
start = bisection_L_Method(0, n - 1)
if  L0 and not Ln:
    count += start + 1
elif L0 and Ln:
    count += n
if  Rn and not R0:
    count += n - bisection_R_Method(start, n - 1)
elif R0 and Rn:
    count += n
print(n - count)
