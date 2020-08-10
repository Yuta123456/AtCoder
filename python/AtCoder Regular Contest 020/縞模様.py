from collections import Counter
n,c = map(int, input().split())
odd = []
even = []
ans = 0
even_count = 0
odd_count = 0
for i in range(n):
    if i % 2 == 0:
        odd.append(int(input()))
        odd_count += 1
    else:
        even.append(int(input()))
        even_count += 1
odd = Counter(odd)
even = Counter(even)
odd = [[i, odd[i]] for i in odd.keys()]
even = [[i, even[i]] for i in even.keys()]
odd.sort(reverse=True, key=lambda x: x[1])
even.sort(reverse=True, key=lambda x: x[1])
if odd[0][0] != even[0][0]:
    ans = (odd_count - odd[0][1]) + (even_count - even[0][1])
elif len(odd) == 1 and len(even) == 1:
    ans = min(even_count,odd_count)
elif len(odd) == 1:
    ans = even_count - even[1][1]
elif len(even) == 1:
    ans = odd_count - odd[1][1]
elif odd[0][1] > even[0][1]:
    ans = (odd_count - odd[0][1]) + (even_count - even[1][1])
else:
    ans = (odd_count - odd[1][1]) + (even_count - even[0][1])
print(ans*c)