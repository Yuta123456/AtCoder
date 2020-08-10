n = int(input())
t = list(map(int, input().split()))
a = list(map(int, input().split()))
mod = 10**9 + 7
#どちらかの値が切り替わってるところは、1通りしかなく、そこが矛盾している場合は弾く
h = [-1 for i in range(n)]
t = [0] + t
a += [0]
for i in range(n):
    if t[i+1] != t[i]:
        h[i] = t[i+1]
for i in range(n,0,-1):
    if h[i-1] != -1 and h[i-1] > a[i-1]:
        print(0)
        exit()
    if a[i] != a[i-1]:
        if h[i-1] == -1:
            h[i-1] = a[i-1]
        else:
            if h[i-1] != a[i-1]:
                print(0)
                exit()
ans = 1
for i in range(n):
    if h[i] == -1:
        #print("index:{} t:{} a:{}".format(i,t[i+1], a[i]))
        ans *= min(t[i+1], a[i])
        ans %= mod
print(ans)
