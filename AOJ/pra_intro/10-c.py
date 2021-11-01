import math
while True:
    n = int(input())
    if n == 0:
        break
    nlist = list(map(int, input().split()))
    avg = sum(nlist) / len(nlist)
    vsum = 0
    for num in nlist:
        vsum += (num - avg)**2
    print(math.sqrt(vsum/n))
