n = input()
if len(n) == 1:
    print(n)
    exit()
if n[0] == '1':
    ans = 0
    judge = set(n[1:])
    if len(judge) == 1 and '9' in judge:
        for i in n:
            ans += int(i)
        print(ans)
    else:
        ans = 9 * (len(n) - 1)
        print(ans)
else:
    ans = int(n[0]) - 1
    for i in range(1,len(n)):
        ans += 9
    print(ans)

