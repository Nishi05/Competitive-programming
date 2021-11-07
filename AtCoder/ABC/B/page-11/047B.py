w, h, n = map(int, input().split())

lw = [0]*w
lh = [0]*h

for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        lw[:x] = [1]*x
    elif a == 2:
        lw[x:] = [1]*(w-x)
    elif a == 3:
        lh[:y] = [1]*y
    elif a == 4:
        lh[y:] = [1]*(h-y)


print(lw.count(0)*lh.count(0))
