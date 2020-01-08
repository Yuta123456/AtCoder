n = int(input())
c = input()
com_dict = dict()
for i in range(n-1):
    temp = c[i] + c[i+1]
    if temp in com_dict:
        com_dict[temp] += 1
    else:
        com_dict[temp] = 1
com_list = list(com_dict.items())
max_com = max(com_list, key=lambda x:x[1])
c = c.replace(max_com[0], "L")

com_dict = dict()
for i in range(len(c)-1):
    if c[i] == "L" or c[i+1] == "L":
        continue
    temp = c[i] + c[i+1]
    if temp in com_dict:
        com_dict[temp] += 1
    else:
        com_dict[temp] = 1
com_list = list(com_dict.items())
max_com = max(com_list, key=lambda x:x[1])
c = c.replace(max_com[0], "R")

print(len(c))
