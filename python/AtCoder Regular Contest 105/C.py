n, m = map(int, input().split())
w = list(map(int, input().split()))
data = []
from itertools import permutations
from bisect import bisect_left
for i in range(m):
    data.append(list(map(int, input().split())))
data.sort(key = lambda x:x[1])
#####segfunc######
def segfunc(x,y):
    return max(x,y)

def init(init_val):
    #set_val
    for i in range(len(init_val)):
        seg[i+num-1]=init_val[i]   
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele = 0
num =2**(m-1).bit_length()
seg=[ide_ele]*(2*num - 1)
#阪堺区間に注意
length = [data[i][0] for i in range(m)]
init(length)
print(length)
weight = [-1] + [data[i][1] for i in range(m)] + [10**18]
length = [-1] + [data[i][0] for i in range(m)] + [10**18]
ans = 10**18
print("weight",weight)
print("length",length)
for per in permutations(w):
    check = []
    can = True
    rakuda = 0
    now = 0
    now_span = 0
    while rakuda < n:
        now += per[rakuda]
        rakuda += 1
        #print("now_weight",now, " now_span",now_span)
        index = bisect_left(weight, now)
        check.append("index:{} weight:{}".format(index, now))
        if index == 1:
            continue
        elif rakuda == 1 and index >= m+1:
            can = False
            break
        else:
            min_span = query(0, index-1)
            now_span += min_span
            now = 0
            rakuda -= 1
        check.append("now_span:{}".format(now_span))
        
    if can:
        ans = min(ans, now_span)
        if now_span == 2909:
            print(check)
print(ans)
