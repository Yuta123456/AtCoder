n,k = map(int, input().split())
data = []
kind = set(range(1,n+1))
for i in range(k):
    d = int(input())
    li = list(map(int, input().split()))
    for j in li:
        if j in kind:
            kind.remove(j)
print(len(kind))
        