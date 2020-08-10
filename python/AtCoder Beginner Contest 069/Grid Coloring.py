h, w = list(map(int, input().split()))
n = int(input())
ans = [[0 for i in range(w)] for j in range(h)]
dec = 1
p = 1
cnt = 0
index = 0
a = list(map(int, input().split()))
for i in range(h):
    while 0 <= index < w:
        if cnt == a[p-1]:
            p += 1
            cnt = 0
        ans[i][index] = p
        cnt += 1
        index += dec
    dec *= (-1)
    index += dec
for i in range(h):
    for j in range(w):
        print("{} ".format(ans[i][j]), end = '')
    print()
    