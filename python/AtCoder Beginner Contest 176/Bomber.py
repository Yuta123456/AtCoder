from collections import defaultdict
h, w, m = map(int, input().split())
target = []
point = defaultdict(int)
count_target_of_y = defaultdict(int)
count_target_of_x = defaultdict(int)
for i in range(m):
    x, y = map(int, input().split())
    count_target_of_y[y] += 1
    count_target_of_x[x] += 1
    point[(x,y)] += 1
max_x_count = max(list(count_target_of_x.items()), key=lambda x:x[1])[1]
max_y_count = max(list(count_target_of_y.items()), key=lambda x:x[1])[1]
max_x_count_list = [i for i in count_target_of_x.items() if i[1] == max_x_count]
max_y_count_list = [i for i in count_target_of_y.items() if i[1] == max_y_count]
for x in max_x_count_list:
    for y in max_y_count_list:
        if point[(x[0], y[0])] == 0:
            print(max_x_count + max_y_count)
            exit()
print(max_x_count + max_y_count - 1)
