t = int(input())
from collections import defaultdict
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    # xor が0になりえない
    dic = defaultdict(int)
    for i in a:
        dic[i] += 1
    even = True
    for v in dic.values():
        if v % 2 != 0:
            even = False
    
    if n % 2 == 0:
        if even:
            print("Second")
        else:
            print("First")
    else:
        if not even:
            print("Second")
        else:
            print("First")
    
    # 交互にコインを入れていき、最終的に、自分の番に、xorが0でスタートしたら勝ち、じゃなきゃ負け
