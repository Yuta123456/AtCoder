import copy
n, m = map(int, input().split())
s = list(input())
s.reverse()
ans = []
cur_index = 0
while cur_index < n:
    pre = copy.deepcopy(cur_index)
    for i in range(min(m, n - cur_index), 0, -1):
        if s[cur_index + i] == '0':
            cur_index += i
            ans.append(i)
            break
    if pre == cur_index:
        print(-1)
        exit()
ans.reverse()
for i in ans:
    print("{} ".format(i), end = "")