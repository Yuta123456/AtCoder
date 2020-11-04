n = int(input())
data = []
in_out = set()

for i in range(n):
    p,q = map(int, input().split())
    if (p != -1 and  q != -1) and q >= p:
        print("No")
        exit()
    else:
        data.append([p,q])

    if p in in_out and p != -1:
        print("No")
        exit()
    if p != -1:
        in_out.add(p)

    if q in in_out and q != -1:
        print("No")
        exit()
    if p != -1:
        in_out.add(q)
# 