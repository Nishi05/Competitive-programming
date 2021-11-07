import math

f, i = math.modf(float(input()))

if f >= 0.5:
    print(int(i)+1)
else:
    print(int(i))
