n,k = map(int, input().split())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
li = factorization(n)
count = 0
for i in range(len(li)):
    count += li[i][1]
if count < k:
    print(-1)
    exit()
ans = ""
rem = n
index = 0
while k >= 1:
    a,b = li[index]
    if k - b <= 1:
        ans += (str(a) + " ") * (k-1)
        rem = rem // pow(a,k-1)
        ans += str(rem)
        break
    else:
        ans += (str(a) + " ") * b
        rem = rem // pow(a,b)
        k -= b
    index += 1
print(ans)

