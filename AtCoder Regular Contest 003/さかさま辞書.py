n = int(input())
str_dict = []
for i in range(n):
    str_dict.append(input())
str_dict.sort(key=lambda x : str(list(reversed(list(x)))))
for i in range(n):
    print(str_dict[i])