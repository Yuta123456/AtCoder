a,b = map(int, input().split())
ans = -1
for i in range(10001):
    if int(i*0.08) == a and int(i*0.1) == b:
        print(i)
        exit()
print(ans)