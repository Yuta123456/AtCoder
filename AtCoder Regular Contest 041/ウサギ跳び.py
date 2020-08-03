n, l = map(int, input().split())
ans = 0
pre_direction = 'R'
rabbit_data = [[0,'R']]
right = 0
left = 0
last_r_point = 1
last_l_point = 1
for i in range(n):
    p, direction = input().split()
    rabbit_data.append([int(p), direction])
rabbit_data.append([l+1, 'L'])

for i in range(n+2):
    print("{} {}".format(i, ans))
    p, direction = rabbit_data[i]
    if pre_direction != direction:
        if pre_direction == 'R':
            last_r_point = rabbit_data[i-1][0]
            left += 1
            last_l_point = p
        else:
            if right < left:
                index = i - (left - 1)
                while rabbit_data[index][1] == 'L':
                    ans += rabbit_data[index][0] - last_r_point
                    last_r_point += 1
                    index += 1
            else:
                index = i - (left + right - 1)
                while rabbit_data[index][1] == 'R':
                    ans += last_l_point - rabbit_data[index][0]
                    last_l_point -= 1
                    index += 1
    else:
        if direction == 'R':
            right += 1
        else:
            left += 1
    pre_direction = direction
if right < left:
    index = n - (left - 1)
    while index < n and rabbit_data[index][1] == 'L':
        ans += rabbit_data[index][0] - last_r_point - 1
        last_r_point += 1
        index += 1
else:
    index = n + 1 - (left + right)
    while index < n and rabbit_data[index][1] == 'R':
        ans += (last_l_point - rabbit_data[index][0] - 1)
        last_l_point -= 1
        index += 1
print(ans)


    