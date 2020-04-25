n = int(input())
flag = True
for i in range(2,int(n**0.5) + 1):
    if n % i == 0:
        flag = False
s = str(n)
if n == 1:
    print("Not Prime")
    exit()
if flag:
    print("Prime")
    exit()
sum_digit = 0
flag = True
for i in range(len(s)):
    sum_digit += int(s[i])
if sum_digit % 3 == 0 or int(s[-1]) % 2 == 0 or s[-1] == '5':
    flag = False 
if flag:
    print("Prime")
else:
    print("Not Prime")