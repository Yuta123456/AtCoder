n, k = map(int, input().split())
a = list(map(int, input().split()))
stand_bit = [set() for i in range(42)]
acc = [0 for i in range(n+1)]
acc[0] = 0
for i in range(1, n+1):
    acc[i] += a[i-1] + acc[i-1]
set_ans = set()
for i in range(n):
    for j in range(i, n):
        set_ans.add(acc[j+1] - acc[i])
        s = acc[j+1] - acc[i]
        index = 41
        while s:
            if s & 1:
                stand_bit[index].add(acc[j+1] - acc[i])
            s = s >> 1
            index -= 1
for i in range(42):
    if len(set_ans & stand_bit[i]) >= k:
        set_ans &= stand_bit[i]
ans_list = list(set_ans)
ans = ans_list[0]
for i in ans_list:
    ans &= i
print(ans)
