import itertools
n = int(input())
a = list(map(int, input().split()))
a = [0] + a
lacc = list(itertools.accumulate(a))
a.reverse()
racc = list(itertools.accumulate(a))
racc = [0] + racc[:-1] 
racc.reverse()
ans = racc[0]
for i in range(n+1):
    ans = min(ans, abs(racc[i] - lacc[i]))
print(ans)