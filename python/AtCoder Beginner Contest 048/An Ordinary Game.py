s = input()
if s[0] == s[-1]:
    #最終的にababa...aの場合
    if len(s) % 2 == 1:
        print("Second")
    else:
        print("First")
else:
    #最終的にababa..bの場合
    if len(s) % 2 == 0:
        print("Second")
    else:
        print("First") 