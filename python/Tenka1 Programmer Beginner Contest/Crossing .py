n = int(input())
#0,n-1が空席かどうかを確認する
print(0)
start = input()
if start == 'Vacant':
    print(0)
    exit()
print(n-1)
last = input()
if last == 'Vacant':
    print(n-1)
    exit()
left_seat = start
right_seat = last
def binary_search(left, right):
    global left_seat
    global right_seat
    mid = (left+right) // 2
    print(mid)
    query = input()
    num = mid - left
    #numの偶奇により判定
    if query == 'Vacant':
        exit()
    if num % 2 == 0:
        if query == left_seat:
            left_seat = query
            binary_search(mid,right)
        else:
            binary_search(left,mid)
    else:
        if query == left_seat:
            binary_search(left,mid)
        else:
            left_seat = query
            binary_search(mid,right)
binary_search(0,n-1)