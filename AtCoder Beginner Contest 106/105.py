n = int(input())
count = 0
def divCount(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt
for i in range(1,n + 1):
    if i%2 != 0:
        if divCount(i) == 8:
            count += 1
print(count)
