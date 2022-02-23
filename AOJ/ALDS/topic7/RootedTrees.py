n = int(input())
tree = [[None] for _ in range(n)]
root = set(range(n))


def set_info(a, i, p, d):
    a[i][1], a[i][2] = p, d
    for j in a[i][0]:
        set_info(a, j, i, d + 1)


for i in range(n):
    val = list(map(int, input().split()))
    tree[val[0]] = [val[2:], None, None]
    root -= set(val[2:])


set_info(tree, root.pop(), -1, 0)

for i in range(n):
    c, p, d = tree[i]
    if p == -1:
        t = 'root'
    elif len(c) == 0:
        t = 'leaf'
    else:
        t = 'internal node'
    print("node ", i, ": parent = ", p,
          ", depth = ", d, ", ", t, ", ", c, sep="")
