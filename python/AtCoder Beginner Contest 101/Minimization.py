n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
if k >= n:
    print(1)
    exit()
count = 0
while n > 0:
    n -= k
    if n > 0:
        n += 1
    
    count += 1
print(count)
