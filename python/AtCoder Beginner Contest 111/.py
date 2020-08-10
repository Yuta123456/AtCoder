import collections
n = int(input())
v = list(map(int, input().split()))
even = []
odd = []
for i in range(n):
    if i % 2 == 0:
        even += [v[i]]
    else:
        odd += [v[i]]
even_dict = collections.Counter(even)
odd_dict = collections.Counter(odd)
max_even = max(even_dict.items(), key = lambda x:x[1])
max_odd = max(odd_dict.items(), key = lambda x:x[1])
#最高の値が同じでない
if max_even[0] != max_odd[0]:
    print(len(even) - max_even[1] + len(odd) - max_odd[1])
else:
    #同じだった場合
    if max_even[1] == len(even) and max_odd[1] == len(odd):
        second_even = (-1,0)
        second_odd = (-1,0)
    elif max_even[1] == len(even):
        second_even = (-1,0)
        second_odd = max([i for i in odd_dict.items() if i != max_odd], key = lambda x:x[1])
    elif max_odd[1] == len(odd):
        second_even = max([i for i in even_dict.items() if i != max_even], key = lambda x:x[1])
        second_odd = (-1,0)
    else:
        second_even = max([i for i in even_dict.items() if i != max_even], key = lambda x:x[1])
        second_odd = max([i for i in odd_dict.items() if i != max_odd], key = lambda x:x[1])
    #二つ目に大きいやつも同じかどうか
    if second_even[1] > second_odd[1]:
        print(len(even) - second_even[1] + len(odd) - max_odd[1])
    else:
        print(len(even) - max_even[1] + len(odd) - second_odd[1])


