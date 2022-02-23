n = int(input())
A = [0] + [int(i) for i in input().split()]

for i in range(1, n + 1):
    s = "node {}: key = {}, ".format(i, A[i])
    if i/2 >= 1:
        s += "parent key = {}, ".format(A[int(i/2)])
    if 2 * i <= n:
        s += "left key = {}, ".format(A[int(2 * i)])
    if 2 * i + 1 <= n:
        s += "right key = {}, ".format(A[int(2 * i + 1)])
    print(s)
