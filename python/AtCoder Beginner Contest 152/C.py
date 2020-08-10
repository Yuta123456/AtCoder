n = int(input())
p = list(map(int, input().split()))
cur_min = 10**7
ans = 0
for i in range(n):
    if cur_min > p[i]:
        cur_min = p[i]
        ans += 1
        
print(ans)