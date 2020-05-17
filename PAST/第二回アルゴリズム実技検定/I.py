n = int(input())
a = list(map(int, input().split()))
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
ide_ele = 2**(n+1)
num =2**(len(a)-1).bit_length()
seg=[ide_ele]*(2*num - 1)
#阪堺区間に注意
init(a)
plus = 2**n-1
for i in range(1<<n):
    seg_index = plus + i
    ans = 0
    while seg_index != 0 and seg[seg_index] == a[i]:
        ans += 1
        if seg_index % 2 == 0:
            seg_index = (seg_index - 2) // 2
        else:
            seg_index = (seg_index - 1) // 2
    print(min(ans,n))