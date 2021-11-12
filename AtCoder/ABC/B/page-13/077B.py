# 直接平方根を見てそれがintだった場合を見ると、直接二乗を見るより計算量が少なくなる

import math
n = int(input())
for i in range(n, 0, -1):
    if float.is_integer(math.sqrt(i)):
        print(i)
        break
