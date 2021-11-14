# int判定 float.is_integer()
import math
a, b = map(str, input().split())

n = int(a+b)

if float.is_integer(math.sqrt(n)):
    print("Yes")
else:
    print("No")
