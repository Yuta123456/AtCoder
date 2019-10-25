n = int(input())
h = list(map(int, input().split()))
global count
count = 0
def calc(data):
    if len(data) == 0:
        return 0
    if min(data) > 0:
        data = list(map(lambda x:x - 1, data))
        global count
        count += 1
        calc(data)
    else:
        k = data.index(min(data))
        calc(data[0:k])
        calc(data[k+1:])
calc(h)
print(count)
