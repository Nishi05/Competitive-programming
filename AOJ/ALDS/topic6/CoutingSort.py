n = int(input())
A = list(map(int, input().split()))


def counting_sort(A, k):
    C = [0]*(k+1)
    B = [0]*(len(A)+1)
    for i in range(0, n):
        C[A[i]] += 1

    for j in range(1, k+1):
        C[j] += C[j-1]

    for k in range(n - 1, -1, -1):
        B[C[A[k]]] = A[k]
        C[A[k]] -= 1
    return B[1:]


print(*counting_sort(A, 10000))
