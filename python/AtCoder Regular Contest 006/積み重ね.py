n = int(input())
weight_list = [0]
for i in range(n):
    weight_list.sort()
    flag = True
    w = int(input())
    for j in range(len(weight_list)):
        if weight_list[j] >= w:
            weight_list[j] = w
            flag = False
            break
    if flag:
        weight_list.append(w)
print(len(weight_list)-1)
