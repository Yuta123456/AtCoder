import itertools
n, k = map(int, input().split())
d = set(list(map(int, input().split())))
inzero = False
if 0 in d:
    inzero = True
    d -= set([0])
can_use = set([0,1,2,3,4,5,6,7,8,9]) - d
can_use = list(can_use)
#全探索
ans = 10**6
def check(i):
    global ans
    x = int("".join(list(map(str, i))))
    if inzero:
       pp = list(str(x))
       if '0' in pp:
           return
    if x >= n:
        ans = min(ans, x)
def dfs(Sequence):
    if len(Sequence) == len(str(n)) + 1:
        check(Sequence)
    else:
        for i in can_use:
            dfs(Sequence + [i])
dfs([])
print(ans)

