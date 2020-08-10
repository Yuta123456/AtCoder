s = list(input())
flag = True
while flag:
    depth = 0
    index_start = 0
    index_goal = 0
    max_depth = 0
    flag = False
    for i in range(len(s)):
        if s[i] == '(':
            flag = True
            if depth + 1 >= max_depth:
                max_depth = depth + 1
                index_start = i
            depth += 1
        elif s[i] == ')':
            if depth == max_depth:
                index_goal = i
            depth -= 1
    if flag:
        insert_string = s[index_start+1:index_goal] + list(reversed(s[index_start+1:index_goal]))
        s = s[:index_start] + insert_string + s[index_goal+1:]
print("".join(s))

    
