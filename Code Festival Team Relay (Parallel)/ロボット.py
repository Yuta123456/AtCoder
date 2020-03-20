import itertools
s = input()
g_x, g_y = map(int, input().split())
cand = itertools.permutations(range(3))
for i in cand:
    