e = list(map(int, input().split()))
b = int(input())
l = list(map(int, input().split()))
if len(set(e) & set(l)) == 6:
    print("1")
elif len(set(e + [b]) & set(l)) >= 6:
    print("2")
elif len(set(e) & set(l)) >= 5:
    print("3")
elif len(set(e) & set(l)) >= 4:
    print("4")
elif len(set(e) & set(l)) >= 3:
    print("5")
else:
    print("0")