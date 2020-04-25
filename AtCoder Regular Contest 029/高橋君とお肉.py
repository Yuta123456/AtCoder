n = int(input())
t = []
for i in range(n):
    t.append(int(input()))
if n == 1:
    print(t[0])
elif n == 2:
    print(max(t))
elif n == 3:
    print(max(max(t), sum(t) - max(t)))
else:
    #1-4 2-3ペア
    t.sort()
    k = max(t[0] + t[3], t[1] + t[2])
    #1-3 2-4ペア
    l = max(t[0] + t[2], t[1] + t[3])
    p = max(t[3], sum(t) - t[3])
    print(min(l,k,p))