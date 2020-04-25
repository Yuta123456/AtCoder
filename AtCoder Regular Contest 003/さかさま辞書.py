n = int(input())
str_dict = []
for i in range(n):
    k = list(input())
    k.reverse()
    k = "".join(k)
    str_dict.append(k)
str_dict.sort()
for i in range(n):
    k = list(str_dict[i])
    k.reverse()
    str_dict[i] = "".join(k)
for i in range(n):
    print(str_dict[i])