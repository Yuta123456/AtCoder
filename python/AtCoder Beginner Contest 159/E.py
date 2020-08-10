h,w,k = map(int, input().split())
choco = []
ans = 10**9
for i in range(h):
    choco.append(list(input()))
for bit in range(1 << (h - 1)):
    count = 0
    split_h = []
    for i in range(h-1):
        if (bit >> i) & 1:
            split_h.append(i)
    split_h.append(h-1)
    split_w = []
    preh = 0
    for cut_h in split_h:
        for i in range(w):
            for j in range(preh, cut_h + 1):
                




    
    