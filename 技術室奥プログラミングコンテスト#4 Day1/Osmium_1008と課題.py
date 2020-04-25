n,m,k,e = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
index = 0
ans = 0
for i in range(n):
    if e >= a[i]:
        e -= a[i]
    else:
        while e < a[i]:
            ans += 1
            if index >= m:
                print("No")
                print(i)
                exit()
            e += b[index]
            index += 1
            if ans > k:
                print("No")
                print(i)
                exit()
        e -= a[i]
print("Yes")
print(ans)

