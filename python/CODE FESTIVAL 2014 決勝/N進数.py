a = int(input())

for i in range(10,a+1):
    k = str(i)
    count = 0
    for j in range(len(k)):
        count += pow(i, len(k)-j-1) * int(k[j])
    if count == a:
        print(i)
        exit()
    if count > a:
        print(-1)
        exit()
print(-1)