n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_cnt = 0
b_cnt = 0
for i in range(n):
    if a[i] > b[i]:
        b_cnt += (a[i] - b[i])
    elif a[i] < b[i]:
        k  = (b[i] - a[i])
        if k % 2 == 0:
            a_cnt += k//2
        else:
            b_cnt += 1
            a_cnt += (k+1)//2
if a_cnt >= b_cnt:
    print("Yes")
else:
    print("No")

