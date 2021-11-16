# シェルソート
n = int(input())
lst = [int(input()) for _ in range(n)]


def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v


def shellSort(A, n):
    g = []
    h = 1
    while h <= len(A):
        g.append(h)
        h = 3*h + 1
    g.reverse()
    m = len(g)
    print(m)
    print(' '.join(map(str, g)))
    for i in range(m):
        insertionSort(A, n, g[i])


cnt = 0

shellSort(lst, n)
print(cnt)
print(*lst, sep="\n")
