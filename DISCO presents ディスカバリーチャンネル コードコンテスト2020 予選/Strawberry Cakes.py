from copy import deepcopy
h,w,k = map(int, input().split())
strawberry_count = [0 for i in range(h)]
cakes = []
for i in range(h):
    cakes.append(list(input()))
    strawberry_count[i] = cakes[i].count('#')
ans = []
first_index = 10000
use_number = 0
for i in range(h):
    append_array = []
    if strawberry_count[i] >= 2:
        first_index = min(first_index,i)
        use_number += 1
        first = True
        for j in range(w):
            if cakes[i][j] == '#':
                if first:
                    first = False
                else:
                    use_number += 1
            append_array.append(use_number)
    elif strawberry_count[i] == 1:
        use_number += 1
        first_index = min(first_index,i)
        append_array = [use_number for i in range(w)]
    else:
        append_array = []
    ans.append(append_array)
print_count = 0
pre_array = []
for i in range(h):
    if len(ans[i]) == 0:
        if print_count > 0:
            print(" ".join(map(str,pre_array)))
        else:
            print(" ".join(map(str,ans[first_index])))
            pre_array = ans[first_index]
            print_count += 1
    else:
        print(" ".join(map(str, ans[i])))
        pre_array = ans[i]
        print_count += 1

