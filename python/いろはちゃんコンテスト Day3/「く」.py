n = int(input())
left = 0
right = 0
ans = 0
c = []
for i in range(n):
    c.append(input())
c = ['.'] + c
for i in range(1,n+1):
    if c[i] == '/':
        if c[i-1] != '/':
            right = 0
        left += 1
    else:
        right += 1
        if left == right:
            ans += 1
            left = 0
    print("left:{} right:{} count:{} ans{}".format(left,right,i,ans))

print(ans)