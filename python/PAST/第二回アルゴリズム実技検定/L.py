n,k,d = map(int, input().split())
a = list(map(int, input().split()))
#####segfunc######
def segfunc(x,y):
    if x[0] == y[0]:
        if x[1] < y[1]:
            return x
        else:
            return y
    elif x[0] < y[0]:
        return x
    else:
        return y

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
ide_ele = [10**10,0]
num =2**(n-1).bit_length()
seg=[ide_ele]*(2*num - 1)
#阪堺区間に注意
init_array = [[a[i],i] for i in range(n)]
init(init_array)
ans = []
left = 0
right = n - d * (k-1)
if left >= right:
    print(-1)
    exit()
for i in range(1,k+1):
    #print("left: {}  right: {}".format(left, right))
    word = query(left, right)
    ans.append(word[0])
    index = word[1]
    right = n - d * (k-i-1)
    left = index + d
for i in range(k):
    print(ans[i], end = " ")
