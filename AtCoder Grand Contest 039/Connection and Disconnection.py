import copy
s = list(input())
k = int(input())
t = copy.deepcopy(s)
transCount = 0
#大体の奴
if s[0] == s[-1]:
    for i in range(len(t) - 2):
        if t[i] == t[i + 1]:
            transCount += 1
            t[i + 1] = '.'
    transCount *= k - 1
    transCount += k - 1
else:
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            transCount += 1
            t[i + 1] = '.'
    transCount *= k - 1
    
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        transCount += 1
        s[i + 1] = '.'
print(transCount)