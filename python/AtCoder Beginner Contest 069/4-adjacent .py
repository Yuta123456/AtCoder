n = int(input())
a = list(map(int, input().split()))
#4で割れる数、2で割れるかず、そうでない数をそれぞれ数えるためのカウント
count_4 = 0
count_2 = 0
count = 0
for i in range(n):
    if a[i] % 4 == 0:
        count_4 += 1
    elif a[i] % 2 == 0:
        count_2 += 1
    else:
        count += 1
if count_2 == 0:
    count_4 += 1
if count_4 >= count :
    print("Yes")
else:
    print("No")
