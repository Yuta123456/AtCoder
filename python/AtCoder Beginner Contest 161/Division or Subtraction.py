n = int(input())
ans = set()
#n-1の約数は確定でOK

for i in range(1,int(pow(n-1,0.5)) + 1):
    if (n-1) % i == 0:
        ans.add((n-1)//i)
        ans.add(i)
#n = (1 + pk) * k^q の形になるkを探す。q ≠ 0のとき、kはnの約数
for i in range(2,int(pow(n,0.5)) + 1):
    if n % i == 0:
        tmp = n
        while tmp % i == 0:
            tmp = tmp // i
        if (tmp - 1) % i == 0:
            ans.add(i)
print(len(ans))

