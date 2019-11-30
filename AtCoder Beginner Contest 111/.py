import collections
n = int(input())
v = list(map(int, input().split()))
even = []
even_c = 0
odd = []
odd_c = 0
ans = 0
for i in range(len(v)):
    print(i)
    if i % 2 == 0:
        even.append(v[i])
        even_c += 1
    else:
        odd.append(v[i])
        odd_c += 1
        
even = collections.Counter(even)
odd = collections.Counter(odd)
even_max = max(list(even.items()), key = lambda x: x[1])
odd_max = max(list(odd.items()), key = lambda x: x[1])
if even_max[0] == odd_max[0]:
    even_sec = [i for i in list(even.items()) if i[0] != even_max[0]] 
    odd_sec = [i for i in list(odd.items()) if i[0] != odd_max[0]]
    if len(even_sec) == 0 and len(odd_sec) == 0:
        print(min(even_max[1], odd_max[1]))
        exit()
    if len(even_sec) == 0:
        ans += min(even_max[1], odd_c - odd_max[1])
        print(ans)
        exit()
    if len(odd_sec) == 0:
        ans += min(odd_max[1], even_c - even_max[1])
        print(ans)
        exit()
    even_sec = max(even_sec, key = lambda x: x[1])
    odd_sec = max(odd, key = lambda x: x[1])
    if even_max[1] > odd_max[1]:
        ans += even_c - even_max[1]
        ans += odd_c - odd_sec[1]
    elif even_max[1] < odd_max[1]:
        ans += odd_c - odd_max[1]
        ans += even_c - even_sec[1]
    else:
        if odd_sec[1] < even_sec[1]:
            ans += even_c - even_sec[1]
            ans += odd_c - odd_max[1]
        elif odd_sec[1] > even_sec[1]:
            ans += odd_c - odd_sec[1]
            ans += even_c - even_max[1]
        else:
            ans += even_c - even_max[1]
            ans += odd_c - odd_sec[1]
else:
    ans += even_c - even_max[1]
    ans += odd_c - odd_max[1]
print(ans)
