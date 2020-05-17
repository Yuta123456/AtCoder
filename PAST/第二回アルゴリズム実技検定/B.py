s = input()
a_count = s.count('a')
b_count = s.count('b')
c_count = s.count('c')
if max(a_count,b_count,c_count) == a_count:
    print("a")
    exit()
if max(a_count,b_count,c_count) == b_count:
    print("b")
    exit()
if max(a_count,b_count,c_count) == c_count:
    print("c")
    exit()