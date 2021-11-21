import math


def isprime(x):
    if x == 2:
        return 1
    if x < 2 or x % 2 == 0:
        return 0
    i = 3
    while i <= math.sqrt(x):
        if x % i == 0:
            return 0
        i += 2
    return 1


n = int(input())
lst = list(map(int, input().split()))

print(sum([isprime(i) for i in lst]))
