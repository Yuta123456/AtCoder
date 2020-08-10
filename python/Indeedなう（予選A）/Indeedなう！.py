original = list("indeednow")
original.sort()
for i in range(int(input())):
    k = list(input())
    k.sort()
    if k == original:
        print("YES")
    else:
        print("NO")