import itertools
import copy
s = input()
g_x, g_y = map(int, input().split())
cand = itertools.permutations(range(4))
word = ['D','U','R','L']
if 0 == g_y and 0 == g_x:
    print("Yes")
    exit()
for i in cand:
    now_x = 0
    now_y = 0
    li = copy.deepcopy(s)
    li = li.replace('W',word[i[0]])
    li = li.replace('X',word[i[1]])
    li = li.replace('Y',word[i[2]])
    li = li.replace('Z',word[i[3]])

    for j in range(len(li)):
        if li[j] == 'D':
            now_y -= 1
        if li[j] == 'U':
            now_y += 1
        if li[j] == 'R':
            now_x += 1
        if li[j] == 'L':
            now_x -= 1
        if now_y == g_y and now_x == g_x:
            print("Yes")
            exit()
print("No")
