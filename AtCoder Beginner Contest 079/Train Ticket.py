n = []
s = input()
def culc(cur, op_c,ans):
    if op_c == 3:
        if cur == 7:
            print(ans + "=7")
            exit()
    else:
        culc(cur+int(s[op_c+1]), op_c+1, ans + "+" + s[op_c+1])
        culc(cur-int(s[op_c+1]), op_c+1, ans + "-" + s[op_c+1])
culc(int(s[0]), 0, s[0])