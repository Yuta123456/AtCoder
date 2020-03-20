import copy
s = input()
original = copy.deepcopy(s)
s = list(s)
s.reverse()
s = "".join(s)
s = s.replace('b','x')
s = s.replace('d','b')
s = s.replace('x', 'd')
s = s.replace('q','x')
s = s.replace('p','q')
s = s.replace('x','p')
if s == original:
    print("Yes")
else:
    print("No")
