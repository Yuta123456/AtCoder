def binary_search_2(left, right):
    if right - left <= pow(10,-6):
        return left
    middle = (right + left) / 2
    if is_can_2(middle):
        return binary_search_2(middle, right)
    else:
        return binary_search_2(left, middle)
def is_can_2(middle):
    #何らかの関数
    normal_monster.sort(reverse=True,key=lambda x: x[1] - middle*x[0])
    weight = 0
    magic = 0
    for i in range(5):
        weight += normal_monster[i][0]
        magic += normal_monster[i][1]
    if magic / weight >= middle:
        return True
    else:
        return False
n, m = map(int, input().split())
normal_monster = []
helpful_monster = []
for i in range(n):
    normal_monster.append(list(map(int, input().split())))
for i in range(m):
    helpful_monster.append(list(map(int, input().split())))

def binary_search(left, right,index):
    if right - left <= pow(10,-6):
        return left
    middle = (right + left) / 2
    if is_can(middle,index):
        return binary_search(middle, right,index)
    else:
        return binary_search(left, middle,index)
def is_can(middle,index):
    #何らかの関数
    normal_monster.sort(reverse=True,key=lambda x: x[1] - middle*x[0])
    weight = helpful_monster[index][0]
    magic = helpful_monster[index][1]
    for i in range(4):
        weight += normal_monster[i][0]
        magic += normal_monster[i][1]
    if magic / weight >= middle:
        return True
    else:
        return False
ans = binary_search_2(0,1000001)
#なんかお助けモンスターを使う場合
for i in range(m):
    ans = max(ans, binary_search(0,100001,i))
print(ans)