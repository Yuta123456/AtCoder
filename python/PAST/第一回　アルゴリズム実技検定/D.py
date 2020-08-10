n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if len(set(a)) == len(a):
    print("Correct")
else:
    ans = -1
    nothing = -1
    a.sort()
    for i in range(n-1):
        if a[i + 1] == a[i]:
            ans = a[i]
    nothing = list(set(range(1,n+1)) - set(a))
    print("{} {}".format(ans, nothing[0]))