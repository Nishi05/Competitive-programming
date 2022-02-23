n = int(input())
tree = [None] * n
root = set(range(n))


def set_pd(i, parent, sibling, depth):
    if i == -1:
        return -1
    node = tree[i]
    left, right = node[0], node[1]
    node[2], node[3], node[5] = parent, sibling, depth
    node[4] = (left != -1) + (right != -1)
    height = node[6] = max(set_pd(left, i, right, depth + 1),
                           set_pd(right, i, left, depth + 1)) + 1
    return height


while n:
    i, left, right = list(map(int, input().split()))
    tree[i] = [left, right] + [None] * 5
    root -= {left, right}
    n -= 1

set_pd(root.pop(), -1, -1, 0)

for i, node in enumerate(tree):
    left, right, p, s, deg, dep, h = node
    print('node {}: parent = {}, sibling = {}, degree = {}, depth = {}, '
          'height = {}, {}'.format(
              i, p, s, deg, dep, h, 'root' if not dep else 'internal node' if
              deg else 'leaf'
          ))
