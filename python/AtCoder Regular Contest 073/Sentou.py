n, t = map(int, input().split())
time = list(map(int, input().split()))
sub_list = []
for i in range(1,n):
    sub_list.append(time[i] - time[i-1])

not_water = 0
for i in sub_list:
    if i > t:
        not_water += (i - t) 
print(time[-1] + t - not_water)
