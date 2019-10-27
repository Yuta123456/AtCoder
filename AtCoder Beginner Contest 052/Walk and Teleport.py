n, a, b = list(map(int, input().split()))
x = list(map(int, input().split()))
cost = 0
for i in range(n - 1):
    distance = x[i+1] - x[i]
    if distance * a <= b:
        cost += distance * a
    else:
        cost += b
print(cost)