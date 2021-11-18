import math
n = int(input())


def isprime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        i += 2
    return True


print("Yes") if isprime(n) else print("No")
