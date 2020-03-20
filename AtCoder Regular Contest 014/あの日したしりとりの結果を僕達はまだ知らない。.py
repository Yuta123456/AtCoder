n = int(input())
used = set()
pre = None
for i in range(n):
    w = input()
    if pre == None:
        pre = w
        used.add(w)
        continue
    if w in used or w[0] != pre[-1]:
        if i % 2 == 0:
            print("LOSE")
            exit()
        else:
            print("WIN")
            exit()
    used.add(w)
    pre = w
print("DRAW")
