class Node():
    def __init__(self, parent=-1, left=-1, right=-1):
        self.parent = parent
        self.left = left
        self.right = right


def pre_parse(ns, i):
    if i == -1:
        return
    print(" " + str(i), end="")
    pre_parse(ns, ns[i].left)
    pre_parse(ns, ns[i].right)


def in_parse(ns, i):
    if i == -1:
        return
    in_parse(ns, ns[i].left)
    print(" " + str(i), end="")
    in_parse(ns, ns[i].right)


def post_parse(ns, i):
    if i == -1:
        return
    post_parse(ns, ns[i].left)
    post_parse(ns, ns[i].right)
    print(" " + str(i), end="")


n = int(input())

ns = [Node() for _ in range(n)]

for i in range(n):
    p, left, r = map(int, input().split())
    if left != -1:
        ns[p].left = left
        ns[left].parent = p
    if r != -1:
        ns[p].right = r
        ns[r].parent = p

for i in range(n):
    if ns[i].parent == -1:
        print("Preorder")
        pre_parse(ns, i)
        print()
        print("Inorder")
        in_parse(ns, i)
        print()
        print("Postorder")
        post_parse(ns, i)
        print()
