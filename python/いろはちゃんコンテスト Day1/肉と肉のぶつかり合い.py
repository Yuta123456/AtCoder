n,x,y = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
for i in range(n):
    if i % 2 == 0:
        x += a[i]
    else:
        y += a[i]
if x > y:
    print("Takahashi")
elif x < y:
    print("Aoki")
else:
    print("Draw")
    