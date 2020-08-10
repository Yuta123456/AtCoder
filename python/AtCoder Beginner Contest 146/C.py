a, b, x = map(int,input().split())
def binary_search(left,right):
    #検索範囲が隣り合ってたら、左のほうが答えになる。
    if right - left <= 1:
        return left
    else:
        #検索範囲の真ん中を見る
        middle = (right + left) // 2
        #middleが条件を満たすかどうか見てみる
        if a * middle + b * len(str(middle)) < x:
            #満たすのであれば、検索範囲を右へ
            return binary_search(middle, right)
            #そうでないなら左へ
        elif a * middle + b * len(str(middle)) > x:
            return binary_search(left, middle)
        else:
            #同じだったら、それが答え
            return middle
print(min(binary_search(0,1 + 10**9),10 ** 9))
