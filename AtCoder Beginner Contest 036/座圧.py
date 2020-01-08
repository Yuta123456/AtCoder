n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
num_dict = dict()
sorted_a = sorted(a)
cnt = 0
for i in sorted_a:
    if i not in num_dict:
        num_dict[i] = cnt
        cnt += 1
for i in a:
    print(num_dict[i])