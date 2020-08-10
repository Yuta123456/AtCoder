h, w = map(int, input().split())
def row_cut(p,q):
    res = 10**5
    for i in range(p):
        a = i * q
        b = ((p - i) // 2) * q
        c = (p * q) - a - b
        res = min(res, max(a,b,c) - min(a,b,c))
    return res 
def row_column_cut(p,q):
    res = 10**5
    for i in range(p):
        a = i * q
        b = (q // 2) * (p - i)
        c = (p * q) - a - b
        res = min(res, max(a,b,c) - min(a,b,c))
    return res
cand = [row_cut(h,w), row_cut(w,h), row_column_cut(w,h), row_column_cut(h,w)]
print(min(cand))