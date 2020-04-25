n = int(input())
ans = 0
for i in range(1,555557):
    if len(set(list(str(i)))) == 1:
        ans += 1
    if ans == n:
        print(i)
        exit() 