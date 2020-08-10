n = int(input())
sum = 0
rate = 380000
for i in range(n):
    money ,kind = input().split()
    if kind == "JPY":
        sum += int(money)
    else:
        sum += float(money) * rate
print(sum)
