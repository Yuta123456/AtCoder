import math
a, b, h, m = map(int, input().split())
alpha = 30.0 * h + (30 * m / 60)
beta = m * 6.0
if alpha < beta:
    theta = beta - alpha
else:
    theta = alpha - beta
print(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(theta))))