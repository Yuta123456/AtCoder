a,b,c = map(int, input().split())
if a == b == c:
    if a % 2 == 1:
        print(0)
    else:
        print(-1)
else:
    ans = 0
    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        next_a = b//2 + c//2
        next_b = a//2 + c//2
        next_c = a//2 + b//2
        a = next_a
        b = next_b
        c = next_c
        ans += 1
    print(ans)
    