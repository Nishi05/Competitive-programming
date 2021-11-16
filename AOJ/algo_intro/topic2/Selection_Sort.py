# 選択ソート
n = int(input())

lst = list(map(int, input().split()))


def selectionSort(A, n):
    cnt = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if A[j] < A[minj]:
                minj = j
        if A[i] != A[minj]:
            A[i], A[minj] = A[minj], A[i]
            cnt += 1
    print(' '.join([str(i) for i in A]))
    print(cnt)


selectionSort(lst, n)
