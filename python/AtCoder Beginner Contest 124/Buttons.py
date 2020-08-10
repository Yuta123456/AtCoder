a, b = map(int, input().split())
sum = 0
if a > b:
    sum += a
    a -= 1
else:
    sum += b
    b -= 1
if a > b:
    sum += a
    a -= 1
else:
    sum += b
    b -= 1
print(sum)
