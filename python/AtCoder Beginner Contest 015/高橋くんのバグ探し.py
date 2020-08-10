import itertools
n, k = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
cand = itertools.product(range(k), repeat = n)
for i in cand:
    ans = 0
    for j in range(n):
        ans ^= data[j][i[j]]
    if ans == 0:
        print("Found")
        exit()
print("Nothing")