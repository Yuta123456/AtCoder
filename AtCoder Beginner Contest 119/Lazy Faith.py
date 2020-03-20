import bisect
a,b,q = list(map(int, input().split()))
shine = []
temple = []
inf = 10**11
x = []
for i in range(a):
    shine.append(int(input()))
shine.append(inf)
for i in range(b):
    temple.append(int(input()))
temple.append(inf)
s2t = [0 for i in range(a+1)]
t2s = [0 for i in range(b+1)]
for i in range(a+1):
    index = bisect.bisect_left(temple, shine[i])
    if index >= 1:
        s2t[i] = min(abs(shine[i] - temple[index]), abs(shine[i] - temple[index - 1]))
    else:
        s2t[i] = abs(shine[i] - temple[index])
for i in range(b+1):
    index = bisect.bisect_left(shine, temple[i])
    if index >= 1:
        t2s[i] = min(abs(temple[i] - shine[index]), abs(temple[i] - shine[index - 1]))
    else:
        t2s[i] = abs(temple[i] - shine[index])
ans = [] 
for i in range(q):
    x = int(input())
    shine_index = bisect.bisect_left(shine, x)
    temple_index = bisect.bisect_left(temple, x)
    #shine_index -> 一番近い神社に行く
    if shine_index >= 1:
        B = abs(shine[shine_index-1] - x) + s2t[shine_index-1]
    else:
        B = inf
    A = abs(shine[shine_index] - x) + s2t[shine_index]
    C = abs(temple[temple_index] - x) + t2s[temple_index]
    if temple_index >= 1:
        D = abs(temple[temple_index-1] - x) + t2s[temple_index-1]
    else:
        D = inf
    print(min([A,B,C,D]))
    
