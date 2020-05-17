from itertools import combinations_with_replacement
n,m,q = map(int, input().split())
data = []
ans = 0
for i in range(q):
    data.append(list(map(int, input().split())))
for array in combinations_with_replacement(range(1,m+1),n):
    count = 0
    array = list(array)
    array.sort()
    for i in range(q):
        if array[data[i][1]-1] - array[data[i][0]-1] == data[i][2]:
            count += data[i][3]
    ans = max(ans, count)
print(ans)


