N,R = map(int, input().split())
S = list(input())
perfect = ['o']*N
res = 0
k = 0
r_i = 0
for i in range(N):
    if S[i] == ".":
        r_i = i
while S != perfect:
    if k+R-1 == r_i:
        res += 1
        break
    if S[k] == '.':
        res += 1
        for i in range(k,min(k+R,N)):
            S[i] = 'o'
    else:
        k += 1
        res += 1
print(res)
#.o..o.