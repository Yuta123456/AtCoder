import sys
input = sys.stdin.readline
def segfunc(x,y):
    return x+y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] += x
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
def binary_search(l,r,k):
    if r - l <= 1:
        return l
    else:
        middle = (l + r)//2
        if query(0,middle) > k:
            return binary_search(l,middle,k)
        else:
            return binary_search(middle, r, k)
q = int(input())
#####単位元######
ide_ele = 0
inf = 2*(10**5) + 1
num =2**(inf-1).bit_length()
seg=[ide_ele]*2*num
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        update(x, 1)
    else:
        index = binary_search(0,inf, x-1)
        print(index)
        update(index, -1)
