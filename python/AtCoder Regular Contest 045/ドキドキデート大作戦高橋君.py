n, m = map(int, input().split())
imos = [0 for i in range(n+2)]
data = []
inf = m+1
for i in range(m):
    s, t = map(int, input().split())
    imos[s] += 1
    imos[t+1] -= 1
    data.append([s,t])
#culc imos
for i in range(1,n+1):
    imos[i] += imos[i-1]
imos[0] = inf
#####segfunc######
def segfunc(x,y):
    return min(x,y)

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
ide_ele = inf
num =2**n.bit_length()
seg=[ide_ele]*2*num
init(imos[:-1])
ans_count = 0
ans = []
for i in range(m):
    s, t = data[i]
    if query(s,t+1) >= 2:
        ans.append(i+1)
        ans_count += 1

print(ans_count)
for i in ans:
    print(i)
    

