a,b,k = map(int, input().split())
count = 0
div = max(a,b)
while True:
    if a % div == 0 and b % div == 0:
        count += 1
        if count == k:
            print(div)
            exit()
    div -= 1
