import itertools
n, W = list(map(int, input().split()))
data = [[] for i in range(4)]
base = 0
for i in range(n):
    w, v = map(int, input().split())
    if i == 0:
        base = w
    data[w-base].append(v)
for i in range(4):
    data[i].sort(reverse=True)
    data[i] = list(itertools.accumulate(data[i]))
ans = 0
for r_0 in range(len(data[0])+1):
    for r_1 in range(len(data[1])+1):
        for r_2 in range(len(data[2])+1):
            for r_3 in range(len(data[3])+1):
                if (r_0 * base) + (r_1 * (base + 1)) + (r_2 * (base + 2)) + (r_3 * (base + 3)) <= W:
                    cand = 0
                    if r_0 >= 1:
                        cand += data[0][r_0-1]
                    if r_1 >= 1:
                        cand += data[1][r_1-1]
                    if r_2 >= 1:
                        cand += data[2][r_2-1]
                    if r_3 >= 1:
                        cand += data[3][r_3-1]
                    ans = max(ans, cand)
print(ans)

