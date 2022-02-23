import sys
NIL = -1


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = NIL
        self.left = NIL
        self.right = NIL


class Tree:
    def __init__(self):
        self.root = NIL

    def insert(self,  z: Node):
        y = NIL
        x = self.root

        while x != NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        z.parent = y

        if y == NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def find(self, key):
        x = self.root
        while x != NIL and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def in_order(self, node: Node):
        if node == NIL:
            return
        self.in_order(node=node.left)
        print(' ' + str(node.key), end='')
        self.in_order(node=node.right)

    def pre_order(self, node: Node):
        if node == NIL:
            return
        print(' ' + str(node.key), end='')
        self.pre_order(node=node.left)
        self.pre_order(node=node.right)

    def show(self):
        self.in_order(self.root)
        print()
        self.pre_order(self.root)
        print()


n = int(input())
T = Tree()

for _ in range(n):
    line = sys.stdin.readline().split()

    if len(line) == 1:
        T.show()
    elif line[0] == 'find':
        key = int(line[1])

        if T.find(key) != NIL:
            print('yes')
        else:
            print('no')
    else:
        key = int(line[1])
        T.insert(Node(key))
