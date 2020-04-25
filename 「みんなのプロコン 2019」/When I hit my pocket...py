k, a, b = map(int, input().split())
biscuits = 1
if a + 2 >= b:
    #全てビスケットでいい
    print(1 + k)
else:
    #お金に交換する方がいい
    ans = 0
    change = 0
    if k >= a+1:
        ans += b
        k -= a + 1
    else:
        print(1+k)
        exit()
    change = max(0, k//2)
    ans += change * (b - a) + (k % 2)
    print(ans)
    