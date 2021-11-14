n = int(input())
lst = list(map(int, input().split()))
blst = [False]*n
for a in range(1, 335):
    for b in range(1, 335):
        s = (4*a*b) + (3*a) + (3*b)
        for idx, l in enumerate(lst):
            if s == l:
                blst[idx] = True
        if blst.count(True) == n:
            break
    else:
        continue
    break


print(blst.count(False))
