s = input()
def is_int(s):
    try:
        int(s)
        print(int(s) * 2)
    except ValueError:
        print("error")
is_int(s)