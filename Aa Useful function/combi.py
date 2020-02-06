def combi(x, y):
    if x < y:
        return 0
    if (x,y) in memo:
        return memo[(x,y)]
    else:
        memo[(x,y)]  = math.factorial(x) / (math.factorial(x - y) * math.factorial(y))
        return memo[(x,y)]