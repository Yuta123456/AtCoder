n = int(input())
Gem = list(map(int, input().split()))
Cost = list(map(int, input().split()))
max = 0
for i in range(n):
    if(Gem[i] - Cost[i] > 0):
        max += Gem[i] - Cost[i]
print(max)
