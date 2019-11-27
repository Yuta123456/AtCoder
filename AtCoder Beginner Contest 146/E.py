#尺取り法と累積和
n, k = map(int, input().split())
a = list(map(int, input().split()))
#kを法とする配列を作る
a = [i % k for i in a]
acc_a = [0 for i in range(n+1)]
acc_a[0] = 0
acc_a[1] = a[0]
#kを法とする累積和
for i in range(2,len(a) + 1):
    acc_a[i] = (a[i - 1] + acc_a[i-1]) % k
#print(acc_a)
ans = 0
for i in range(len(acc_a)):
    for j in range(max(0, i - k), i):
        #print("i {}  j {}".format(i,j))
        list_sum = acc_a[i] - acc_a[j]
        if list_sum < 0:
            list_sum += k
        if i - j == list_sum:
            #print("i {}  j {}".format(i,j))
            ans += 1
print(ans)