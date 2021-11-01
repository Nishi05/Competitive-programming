n = int(input())

bt = 0
bx = 0
by = 0
flg = True
for i in range(n):
    t, x, y = map(int, input().split())
    dt = t - bt
    dist = abs(x-bx)+abs(y-by)
    if dt < dist:
        flg = False
        break
    elif dt % 2 != dist % 2:
        flg = False
        break
    else:
        bt = t
        bx = x
        by = y

if flg == True:
    print("Yes")
else:
    print("No")
