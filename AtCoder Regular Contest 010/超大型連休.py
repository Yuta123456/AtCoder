n = int(input())
weekday = [1,2,3,4,5,6,7]
now_month = 1
now_day = 0
ans = 0
holiday = set()
w_index = 5
count = 0
point = 0
for i in range(n):
    s = tuple(map(int, input().split('/')))
    holiday.add(s)
for i in range(366):
    w_index = (1 + w_index) % 7
    now_day += 1
    if now_month in set([1,3,5,7,8,10,12]):
        if now_day > 31:
            now_day = 1
            now_month += 1
    elif now_month in set([4,6,9,11]):
        if now_day > 30:
            now_day = 1
            now_month += 1
    else:
        if now_day > 29:
            now_day = 1
            now_month += 1
    flag = True
    if weekday[w_index] in set([6,7]):
        count += 1
        flag = False
    if (now_month,now_day) in holiday:
        count += 1
        if flag == False:
            point += 1
            count -= 1
        else:
            flag = False
    if flag:
        if point > 0:
            point -= 1
            count += 1
        else:
            count = 0
    ans = max(ans, count)
print(min(ans,366))
