from copy import deepcopy
n = int(input())
data = []
x_candidate = []
y_candidate = []
for i in range(n):
    data.append(list(map(int, input().split())))
    x_candidate.append(data[i][0])
    y_candidate.append(data[i][1])
original = [10**6 for i in range(n)]
for i in range(n):
    original[i] = min(abs(data[i][0]), abs(data[i][1]))
for i in range(n+1):
    min_D = deepcopy(original)
    for p in range(i):
        best_line = (0, 0)
        best_dec = 0
        for x in x_candidate:
            sum_dec = 0
            for j in range(n):
                sum_dec += max(0, min_D[j] - abs(data[j][0] - x)) * data[j][2]
            if sum_dec > best_dec:
                best_dec = sum_dec
                best_line = (x, 0)
        for y in y_candidate:
            sum_dec = 0
            for j in range(n):
                sum_dec += max(0, min_D[j] - abs(data[j][1] - y)) * data[j][2]
            if sum_dec > best_dec:
                best_dec = sum_dec
                best_line = (0, y)
        for j in range(n):
            min_D[j] = min(min_D[j], abs(data[j][0] - best_line[0]), abs(data[j][1] - best_line[1]))
        #print(best_line)
    #print(min_D)
    ans = 0
    for j in range(n):
        ans += min_D[j] * data[j][2]
    print(ans)