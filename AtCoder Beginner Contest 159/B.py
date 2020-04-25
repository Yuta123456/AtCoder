import copy
s = list(input())
n = len(s)
k = copy.deepcopy(s)
k.reverse()
if k != s:
    print("No")
    exit()
formar = copy.deepcopy(s[:(n-1)//2])
q = copy.deepcopy(formar)
q.reverse()
if q != formar:
    print("No")
    exit()
last = copy.deepcopy(s[(n+3)//2 - 1:])
k = copy.deepcopy(last)
k.reverse()
if last != k:
    print("No")
    exit()
print("Yes")
