n, m = map(int, input().split())
data = []
dict_q = dict()
wa = 0
ac = 0
finished = set()
for i in range(m):
    p, s = input().split()
    if s == "WA":
        if p in dict_q:
            dict_q[p] += 1
        else:
            dict_q[p] = 1
    else:
        if p in finished:
            continue
        finished.add(p)
        if p in dict_q:
            wa += dict_q[p]
        ac += 1
print("{} {}".format(ac,wa))
    