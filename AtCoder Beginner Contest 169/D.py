import bisect
n = int(input())
#nを受け取り、nを素因数分解した形で返す
if n == 1:
    print(0)
    exit()
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
acc = [0 for i in range(1000)]
acc[1] = 1
for i in range(2,1000):
    acc[i] = acc[i-1] + i
array = factorization(n)
ans = 0
for num, count in array:
    index = bisect.bisect_right(acc, count)
    ans += (index - 1)
print(ans)
