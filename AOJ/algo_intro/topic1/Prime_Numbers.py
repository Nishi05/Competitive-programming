# 素数
import math


def isprime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i <= int(math.sqrt(x)):
        if x % i == 0:
            return False
        i += 2
    return True


n = int(input())
cnt = 0
for _ in range(n):
    m = int(input())
    if isprime(m):
        cnt += 1
print(cnt)
