n = int(input())
ans = set()
for i in range(n):
    a,b = map(int, input().split())
    if a > b:
        a,b = b,a
    ans.add((a,b))
print(len(ans))