from math import sin, cos, radians

n = int(input())


def koch(p1x, p1y, p2x, p2y, depth):
    if n == depth:
        return
    sx = p1x + (p2x - p1x) / 3
    tx = p1x + (p2x - p1x) / 3*2
    sy = p1y + (p2y - p1y) / 3
    ty = p1y + (p2y - p1y) / 3*2

    ux = sx + (tx-sx) * cos(radians(60)) - (ty-sy) * sin(radians(60))
    uy = sy + (tx-sx) * sin(radians(60)) + (ty-sy) * cos(radians(60))
    koch(p1x, p1y, sx, sy, depth+1)
    print(sx, sy)
    koch(sx, sy, ux, uy, depth+1)
    print(ux, uy)
    koch(ux, uy, tx, ty, depth+1)
    print(tx, ty)
    koch(tx, ty, p2x, p2y, depth+1)


print(0, 0)
koch(0, 0, 100, 0, 0)
print(100, 0)
