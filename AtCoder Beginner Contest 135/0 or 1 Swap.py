n = int(input())
p = tuple(map(int,input().split()))
ans = sorted(p)
for i in range(n):
    for j in range(n):
        ori = list(p)
        temp = ori[i]
        ori[i] = ori[j]
        ori[j] = temp
        if ans == ori:
            print("YES")
            exit()
print("NO")
