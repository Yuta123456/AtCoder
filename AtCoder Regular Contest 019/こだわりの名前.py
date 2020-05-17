a = list(input())
may_be_palindrome = [False for i in range(len(a))]
count = 0
ans = 0
#一文字の場合
if len(a) == 1:
    print(0)
    exit()
for i in range(len(a)//2):
    if a[i] != a[-(i+1)]:
        count += 1
if count >= 2:
    print(25*len(a))
elif count == 1:
    print(24*2 + 25*(len(a)-2))
else:
    if len(a) % 2 == 0:
        print(25*len(a))
    else:
        print(25*(len(a)-1))