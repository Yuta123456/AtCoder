from collections import Counter
n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
kind = list(set(a))
ans_count = dict()
sum_ans = 0
for i in range(len(kind)):
    num = kind[i]
    k = count[num] 
    sum_ans += k*(k-1)//2
for i in range(n):
    ans = sum_ans
    num = a[i]
    k = count[num]
    ans -= k*(k-1) // 2
    ans += (k-1)*(k-2)//2
    print(ans)
