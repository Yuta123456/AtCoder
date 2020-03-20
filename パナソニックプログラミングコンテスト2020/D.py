n = int(input())
def all_search(array):
    if len(array) == n:
        print(array)
    else:
        kind = len(set(array))
        fin = min(kind + 1, len(array) + 1)
        for i in range(fin):
            res = array + chr(i + ord('a'))
            all_search(res)
all_search("")
