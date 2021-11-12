import math


# 人の幅とスペースの幅を足していく。
x, y, z = map(int, input().split())

for i in range(1, x):
    n = (i*y) + ((i+1)*z)
    if n > x:
        print(i-1)
        break
