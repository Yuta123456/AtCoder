s = input()
from itertools import permutations
if len(s) < 8:
    for i in permutations(list(s)):
        i = "".join(i)
        i = int(i)
        if i % 8 ==0:
            print("Yes")
            exit()
    print("No")
    exit()
hachi = []
from collections import defaultdict
for i in range(0,1000,8):
    hachi.append(i)
d = defaultdict(int)
for i in s:
    d[i] += 1
for i in hachi:
    i = str(i).zfill(3)
    p = defaultdict(int)
    for k in i:
        p[k] += 1
    flag = True
    for k, c in p.items():
        if d[k] < c:
            flag = False
            break
    if flag:
        print("Yes")
        exit()
                
        


print("No")