k = int(input())
num = 7
for i in range(k + 2):
    if num % k == 0:
        print(i + 1)
        exit()
    else : 
        num = ( num * 10 + 7 ) % k
print(-1)