n = int(input()) + 1
a = list(map(int, input().split())) + [0]
money = 1000
stock = 0
greater = [False for i in range(n)]
less = [False for i in range(n)]
buy = [False for i in range(n)]
for i in range(n-1):
    greater[i] = ( a[i] < a[i+1] ) 
    less[i] = a[i] > a[i+1]
    if less[i] and i < n-1:
        buy[i+1] = True
for i in range(n):
    if greater[i]:
        count = money // a[i]
        stock += count
        money -= count * a[i]
    if less[i]:
        count = stock
        stock = 0
        money += count * a[i]
print(money) 
