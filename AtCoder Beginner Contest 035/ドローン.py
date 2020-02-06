s = input()
t = input()
count_q = 0
cur_point = [0,0]
for i in s:
    if i == '?':
        count_q += 1
    elif i == 'U':
        cur_point[1] += 1
    elif i == 'D':
        cur_point[1] -= 1
    elif i == 'R':
        cur_point[0] += 1
    else:
        cur_point[0] -= 1
if t == '1':
    print(abs(cur_point[0]) + abs(cur_point[1]) + count_q)
else:
    if abs(cur_point[0]) + abs(cur_point[1]) >= count_q:
        print(abs(cur_point[0]) + abs(cur_point[1]) - count_q)
    else:
        count_q -= abs(cur_point[0]) + abs(cur_point[1])
        print(count_q % 2)