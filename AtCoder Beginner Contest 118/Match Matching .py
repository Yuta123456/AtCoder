n , m = map(int, input().split())
A = list(map(int, input().split()))
A.sort
A.reverse()
table = [0,2,5,5,4,5,6,3,7,6]
min_cost_num = 0
ans = []
min_cost = 10
for i in A:
    if min_cost > table[i]:
        min_cost = table[i]
        min_cost_num = i
    elif min_cost == table[i]:
        if min_cost_num < i:
            min_cost_num = i
while n - min_cost > 0:
    ans.append(min_cost_num)
    n -= min_cost
print(ans)
print(n)
#増やす方向でマッチ棒を減らす
increase = [i for i in A if min_cost_num < i]
while True:
    for i in range(len(ans)):
        

