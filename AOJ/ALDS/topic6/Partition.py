n = int(input())
A = list(map(int, input().split()))


def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]

    return i


r = partition(A, 0, n-1)
ans = [str(i) for i in A]
ans[r] = '[{}]'.format(A[r])
print(*ans)
