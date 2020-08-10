def min_index(bamboo, l):
    min = 1001
    index = 0
    for i in range(len(bamboo)):
        if min > abs(bamboo[i] - l):
            index = i
            min = abs(bamboo[i] - l)
    return index

def calc(bamboo, l,ans):
    min_i = min_index(bamboo, l)
    if abs(bamboo[min_i] - l) <= 10:
        ans += abs(bamboo[min_i] - l)
        del bamboo[min_i]
        return 0
    else:
        if bamboo[min_i] < l:
            k = add_bamboo()
            if k != -1:
                bambo
            else:


n, a, b, c = list(map(int, input().split()))
l = []
for i in range(n):
    l.append(int(input()))
