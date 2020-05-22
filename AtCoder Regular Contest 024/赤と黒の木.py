n = int(input())
c = []
for i in range(n):
    c.append(int(input()))
if c[0] == c[-1]:
    #ややこしいパターン
    start_index = -1
    for i in range(n-1):
        if c[i] != c[i+1]:
            start_index = i+1
            break
    if start_index == -1:
        print(-1)
    else:
        max_length = 0
        count = 1
        for i in range(start_index, start_index + n - 1):
            if c[i%n] == c[(i+1)%n]:
                count += 1
            else:
                max_length = max(count, max_length)
                count = 1
        max_length = max(count, max_length)
        if max_length == n:
            print(-1)
        else:
            print(((max_length-1)//2)+1)
else:
    max_length = 0
    count = 1
    for i in range(n-1):
        if c[i] == c[i+1]:
            count += 1
        else:
            max_length = max(count, max_length)
            count = 1
    max_length = max(count, max_length)
    if max_length == n:
        print(-1)
    else:
        print(((max_length-1)//2)+1)
    