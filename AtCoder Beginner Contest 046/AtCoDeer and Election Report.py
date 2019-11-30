n = int(input())
takahashi = 0
aoki = 0
for i in range(n):
    t, a = map(int, input().split())
    if i == 0:
        takahashi = t
        aoki = a
    else:
        
