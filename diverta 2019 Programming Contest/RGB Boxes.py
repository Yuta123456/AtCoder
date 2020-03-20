R, G, B, N = list(map(int, input().split()))
ans = 0
for b in range(3001):
    for g in range(3001):
        if (N - b*B - g*G) % R == 0 and (N - b*B - g*G) >= 0:
            #print(b,g)
            ans += 1
print(ans) 
