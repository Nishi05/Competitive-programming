# バブルソート
n = int(input())

lst = list(map(int, input().split()))


def bubblesort(A, n):
    flg = 1
    m = 0
    cnt = 0
    while flg:
        flg = 0
        for i in range(n-1, m, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                cnt += 1
                flg = 1
        m += 1
    print(' '.join([str(i) for i in A]))
    print(cnt)


bubblesort(lst, n)
