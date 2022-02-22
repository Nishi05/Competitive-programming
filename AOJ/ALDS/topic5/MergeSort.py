def merge(A, left, mid, right):
    global cnt
    inf = 10**9
    L = A[left:mid] + [inf]
    R = A[mid:right] + [inf]

    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def merge_sort(A, left, right):
    if left + 1 < right:
        mid = (left+right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


n = int(input())
A = list(map(int, input().split()))
cnt = 0
merge_sort(A, 0, n)

print(' '.join(str(i) for i in A))
print(cnt)
