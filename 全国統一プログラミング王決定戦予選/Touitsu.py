n = int(input())
a = input()
b = input()
c = input()
ans = 0
for i in range(n):
    k = set([a[i], b[i],c[i]])
    ans += len(k) - 1
print(ans)